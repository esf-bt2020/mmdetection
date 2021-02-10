﻿using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Text.Json;

using System.Text.Json;
using System.Text.Json.Serialization;

namespace DatasetHandler
{
    class Program
    {
        static void Main(string[] args)
        {
            string rootpath = @"C:\Work\Github\esf-bt2020_mmdetection\customDataCaltech";
            //CreateStrictSplittedCameraLocationsOrigClasses(rootpath);


            string filename = "caltech_bboxes_20200316.json";
            var imagelist = GetImageList(rootpath, filename);


            string sourceFolder = @"Y:\Thesis\Datensets\cct_images";
            string targetfolder = @"Y:\Thesis\Datensets\cct_images_bbox_all";
            CopyFilesInListToTargetFolder(sourceFolder, targetfolder, imagelist);
        }

        private static void CopyFilesInListToTargetFolder(string sourceFolder, string targetFolder, List<string> filenames)
        {
            DirectoryInfo dir = new DirectoryInfo(sourceFolder);
            int copied = 0;
            foreach(var file in filenames )
            {
                string fileFullname = Path.Combine(sourceFolder, file);
                FileInfo fileinf = new FileInfo(fileFullname);
                if ( fileinf.Exists )
                {
                    //Copy file
                    fileinf.CopyTo(Path.Combine(targetFolder, file));
                    copied++;
                }
                else
                {
                    Console.WriteLine("File: " + fileFullname + " does not exist!");
                }

            }

        }

        private static List<string> GetImageList(string path, string filename)
        {
            List<string> list = new List<string>();



            //string jsonString = File.ReadAllText(Path.Combine(path, filename));

            var stream = System.IO.File.Open(Path.Combine(path, filename), System.IO.FileMode.Open);
            System.Text.Json.JsonDocument doc = JsonDocument.Parse(stream);




            foreach (var element in doc.RootElement.EnumerateObject())
            {
                if (element.Name == "images")
                {
                    Console.WriteLine(element.Name);

                    foreach (var img in element.Value.EnumerateArray())
                    {
                        var imageid = img.GetProperty("id").GetString();
                        var location = img.GetProperty("location");
                        var locationint = int.Parse(location.GetString());
                        var filenameImg = img.GetProperty("file_name").ToString();
                        if (!list.Contains(filenameImg))
                        {
                            list.Add(filenameImg);
                        }
                    }
                }
            }

            return list;
        }

        private static void CreateStrictSplittedCameraLocationsOrigClasses(string rootpath)
        {
            string splitdefinition = Path.Combine(rootpath, "CaltechCameraTrapsSplits_v0.json");
            var mapping = GetLocationSetMapping(splitdefinition);

            string imagesFile = Path.Combine(rootpath, "caltech_images_20210113.json");
            var imageMapping = GetSplitDic(imagesFile, mapping);

            string bboxannotations = Path.Combine(rootpath, "caltech_bboxes_20200316_work.json");
            string cleanedannotations = CleanAnnotationFile(bboxannotations);

            SplitAnnotationFile(cleanedannotations, imageMapping);
        }

        private static Dictionary<int, List<string>> GetLocationSetMapping(string path)
        {
            var stream = System.IO.File.Open(path, System.IO.FileMode.Open);
            System.Text.Json.JsonDocument doc = JsonDocument.Parse(stream);

            Dictionary<int, List<string>> dic = new Dictionary<int, List<string>>();


            foreach (var element in doc.RootElement.EnumerateObject())
            {
                if (element.Name == "splits")
                {
                    foreach (var set in element.Value.EnumerateObject())
                    {

                        foreach (var location in set.Value.EnumerateArray())
                        {
                            var strlocationid = location.GetString();
                            var locationid = int.Parse(strlocationid);
                            var setname = set.Name;
                            if (!dic.ContainsKey(locationid))
                            {
                                dic.Add(locationid, new List<string> { setname });
                            }
                            else
                            {
                                var list = dic.GetValueOrDefault(locationid);
                                if (!list.Contains(setname))
                                {
                                    list.Add(setname);
                                }
                            }

                        }
                    }
                }
            }
            return dic;
        }

        private static Dictionary<string,ImageDetail> GetSplitDic(string path, Dictionary<int, List<string>> splitdefinition)
        {
            //string1 = imageId, string2 = set
            var dic = new Dictionary<string, ImageDetail>();

            string jsonString = File.ReadAllText(path);

            var stream = System.IO.File.Open(path, System.IO.FileMode.Open);
            System.Text.Json.JsonDocument doc = JsonDocument.Parse(stream);




            foreach (var element in doc.RootElement.EnumerateObject())
            {
                if (element.Name == "images")
                {
                    Console.WriteLine(element.Name);

                    foreach (var img in element.Value.EnumerateArray() )
                    {
                        var imageid = img.GetProperty("id").GetString();
                        var location = img.GetProperty("location");
                        var locationint = int.Parse(location.GetString());
                        
                        if (splitdefinition.TryGetValue(locationint, out var sets))
                        {
                            var imageDetail = new ImageDetail();
                            imageDetail.CaltechImageId = imageid;
                            imageDetail.CocoConformId = DatasetHandler.GetCOCOMappedImageId(imageid).ToString();
                            imageDetail.TargetDatasets = sets;

                            dic.Add(imageid, imageDetail);

                        }
                        else
                        {

                        }
                    }

                }                
            }
            return dic;
        }

        private static void SplitAnnotationFile(string path, Dictionary<string, ImageDetail> splitDic )
        {


            List<Annotation> trainAnnotations = new List<Annotation>();
            List<Annotation> valAnnotations = new List<Annotation>();
            List<Annotation> eccvTrainAnnotations = new List<Annotation>();
            List<Annotation> eccvvalAnnotations = new List<Annotation>();

            List<Annotation> eccvvalTESTAnnotations = new List<Annotation>();

            List<Image> trainimages = new List<Image>();
            List<Image> valimages = new List<Image>();
            List<Image> eccvtrainimages = new List<Image>();
            List<Image> eccvvalimages = new List<Image>();

            List<Image> eccvvalTESTimages = new List<Image>();


            string jsonString = File.ReadAllText(path);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            Dictionary<string, Image> allImages = new Dictionary<string, Image>();

            foreach(var image in deserialized.images )
            {
                allImages.Add(image.id, image);
            }

            Random r1 = new Random();
            bool excludeHalf = true;
            int counter = 0;
            foreach (var annotations in deserialized.annotations)
            {
                counter++;
                if (excludeHalf)
                {
                    if (int.Parse(annotations.image_id) % 2 == 0)
                    {
                        continue;
                    }
                }

                if ( splitDic.TryGetValue(annotations.image_id_caltech, out var imageDetail) )
                {
                    foreach (var set in imageDetail.TargetDatasets)
                    {
                        Image image = null;
                        switch (set)
                        {
                            case "train":
                                if ( allImages.TryGetValue(annotations.image_id, out image) )
                                {
                                    trainAnnotations.Add(annotations);
                                    if (!trainimages.Contains(image))
                                    {
                                        trainimages.Add(image);
                                    }
                                }
                                break;
                            case "val":
                                if (allImages.TryGetValue(annotations.image_id, out image))
                                {
                                    valAnnotations.Add(annotations);
                                    if (!valimages.Contains(image))
                                    {
                                        valimages.Add(image);
                                    }
                                }
                                break;
                            case "eccv_val":
                                if (allImages.TryGetValue(annotations.image_id, out image))
                                {
                                    int mod = int.Parse(annotations.id) % 3;
                                    if (mod <= 1)
                                    {
                                        eccvvalAnnotations.Add(annotations);
                                        if (!eccvvalimages.Contains(image))
                                        {
                                            eccvvalimages.Add(image);
                                        }
                                    }
                                    else
                                    {
                                        eccvvalTESTAnnotations.Add(annotations);
                                        if (!eccvvalTESTimages.Contains(image))
                                        {
                                            eccvvalTESTimages.Add(image);
                                        }
                                    }
                                }
                                break;
                            case "eccv_train":
                                if (allImages.TryGetValue(annotations.image_id, out image))
                                {
                                    eccvTrainAnnotations.Add(annotations);
                                    if (!eccvtrainimages.Contains(image))
                                    {
                                        eccvtrainimages.Add(image);
                                    }
                                }
                                break;
                        }
                    }
                }
            }

            FileInfo file = new FileInfo(path);
            string outputPath = Path.Combine(file.DirectoryName, "output");
            DirectoryInfo dir = new DirectoryInfo(outputPath);
            if ( !dir.Exists )
            {
                dir.Create();
            }

            deserialized.annotations = trainAnnotations.ToArray();
            deserialized.images = trainimages.ToArray();
            var serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));

            var statstrain = GetCategoryCounterOfAnnotations(deserialized.annotations, "train");

            System.IO.File.WriteAllText(outputPath + @"\train_adv.json", serialized);

            deserialized.annotations = valAnnotations.ToArray();
            deserialized.images = valimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            var stats_val = GetCategoryCounterOfAnnotations(deserialized.annotations, "val");
            System.IO.File.WriteAllText(outputPath + @"\val_adv.json", serialized);

            deserialized.annotations = eccvTrainAnnotations.ToArray();
            deserialized.images = eccvtrainimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            var statseccvtrain = GetCategoryCounterOfAnnotations(deserialized.annotations, "eccv_train");
            System.IO.File.WriteAllText(outputPath + @"\eccv_train_adv.json", serialized);

            deserialized.annotations = eccvvalAnnotations.ToArray();
            deserialized.images = eccvvalimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            var statseccvval = GetCategoryCounterOfAnnotations(deserialized.annotations, "eccv_val");
            System.IO.File.WriteAllText(outputPath + @"\eccv_val_adv.json", serialized);

            deserialized.annotations = eccvvalTESTAnnotations.ToArray();
            deserialized.images = eccvvalTESTimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            var statseccvtest = GetCategoryCounterOfAnnotations(deserialized.annotations, "eccv_val_TEST");
            System.IO.File.WriteAllText(outputPath + @"\eccv_val_TEST_adv.json", serialized);
        }

        private static Dictionary<long, int> GetCategoryCounterOfAnnotations(Annotation[] array, string type)
        {
            Dictionary<long, int> categories = new Dictionary<long, int>();
            foreach (var x in array)
            {
                if (categories.TryGetValue(x.category_id, out var countera))
                {
                    countera++;
                    categories.Remove(x.category_id);
                    categories.Add(x.category_id, countera);
                }
                else
                {
                    categories.Add(x.category_id, 1);
                }
            }
            foreach(var key in categories.Keys )
            {
                Debug.Write(type + ";" + key + ";" + categories.GetValueOrDefault(key));
            }
            return categories;
        }

        private static string CleanAnnotationFile(string path)
        {
           

            string jsonString = File.ReadAllText(path);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);


            foreach(var image in deserialized.images )
            {
                image.id_caltech = image.id;
                image.id = DatasetHandler.GetCOCOMappedImageId(image.id).ToString();
            }
          

            foreach (var annotations in deserialized.annotations )
            {
                var arearaw = (float.Parse(annotations.bbox[2].ToString()) * float.Parse(annotations.bbox[3].ToString()));
                var area = Math.Round(arearaw, 0);
                annotations.iscrowd = 0;
                annotations.area = area;
                annotations.segmentation = new string[0];

                annotations.image_id_caltech = annotations.image_id;
                int cocoId = DatasetHandler.GetCOCOMappedImageId(annotations.image_id);
                annotations.image_id = cocoId.ToString();

                annotations.id_caltech = annotations.id;
                annotations.id = DatasetHandler.GetCOCOMappedAnnotationId(annotations.id).ToString();


            }

            var serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));

            string targetfilename = path + "_cleaned";
            System.IO.File.WriteAllText(targetfilename, serialized);

            return targetfilename;


        }


        private static void Parse(string path)
        {
            var stream = System.IO.File.Open(path, System.IO.FileMode.Open);
            System.Text.Json.JsonDocument doc = JsonDocument.Parse(stream);




            foreach(var element in doc.RootElement.EnumerateObject())
            {
                Console.WriteLine(element.Name);
                if (element.Name == "annotations")
                {
                    //element.
                    foreach (var ann in element.Value.EnumerateArray() )
                    {
                        //Annotation
                        var bbox = ann.GetProperty("bbox");

                        string rawbox = bbox.GetRawText();
                        string[] bboxarray = rawbox.Split(",");

                        var area = (float.Parse(bboxarray[2]) * float.Parse(bboxarray[3]));

             

                    }
                }


            }

        }
    }
}