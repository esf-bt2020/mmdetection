using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class Adv5_GenerateSplitDay1000
    {

        /*
         * Alle Bounding boxen der Typen einlesen inkl. image_id
         * Bounding boxen aufteilen in: tag of jahr modulo 10, 0-6 = train, 7-8 = val, 9=test
         */

        //used in thesis:             string fileToSplit = @"C:\Work\Github\esf-bt2020_mmdetection\customDataCaltech\adv5\caltech_bboxes_20200316_cleaned_with_location.json";

        public static void SplitAnnotationFile(string path)
        {

            List<Annotation> knowntrainAnnotations = new List<Annotation>();
            List<Annotation> knownvalAnnotations = new List<Annotation>();
            List<Annotation> knowntestAnnotations = new List<Annotation>();

            List<Annotation> transvalAnnotations = new List<Annotation>();
            List<Annotation> transtestAnnotations = new List<Annotation>();


            List<Image> knowntrainimages = new List<Image>();
            List<Image> knownvalimages = new List<Image>();
            List<Image> knowntestimages = new List<Image>();

            List<Image> transvalimages = new List<Image>();
            List<Image> transtestimages = new List<Image>();


            string jsonString = File.ReadAllText(path);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            Dictionary<long, Adv5_DatasetHandler> animalStatistics = new Dictionary<long, Adv5_DatasetHandler>();

            Dictionary<string, Image> allImages = new Dictionary<string, Image>();

            foreach (var img in deserialized.images)
            {
                allImages.Add(img.id, img);
            }


            int usedAnnotations = 0;
            int ignoredAnnotationCategory = 0;
            int ignoredAnnotationCount = 0;
            foreach (var annotations in deserialized.annotations)
            {

                if (!Adv5_DatasetHandler.IsAnimalRelevant(annotations.category_id))
                {
                    //Annotation nicht relevant für dataset
                    ignoredAnnotationCategory++;
                    continue;
                }


                Image image = null;
                if (allImages.TryGetValue(annotations.image_id, out image))
                {

                    string type = Adv5_DatasetHandler.GetTargetDatasetOfImage(image);

                    if (animalStatistics.TryGetValue(annotations.category_id, out var stats))
                    {
                        if (stats.IsLimitReached(image, type))
                        {
                            continue;
                        }
                        if (stats.ImagesPerLocation.TryGetValue(image.location, out var list))
                        {
                            list.Add(new ImageDescription() { image = image, type = type });
                        }
                        else
                        {
                            stats.ImagesPerLocation.Add(image.location, new List<ImageDescription>() { new ImageDescription() { image = image, type = type } });
                        }
                    }
                    else
                    {
                        Adv5_DatasetHandler statistics = new Adv5_DatasetHandler();
                        statistics.CategoryId = annotations.category_id;
                        statistics.ImagesPerLocation = new Dictionary<string, List<ImageDescription>>();
                        statistics.ImagesPerLocation.Add(image.location, new List<ImageDescription>() { new ImageDescription() { image = image, type = type } });
                        animalStatistics.Add(annotations.category_id, statistics);
                    }




                    usedAnnotations++;



                    switch (type)
                    {
                        case "known_train":

                            knowntrainAnnotations.Add(annotations);
                            if (!knowntrainimages.Contains(image))
                            {
                                knowntrainimages.Add(image);
                            }
                            break;
                        case "known_val":

                            knownvalAnnotations.Add(annotations);
                            if (!knownvalimages.Contains(image))
                            {
                                knownvalimages.Add(image);
                            }
                            break;
                        case "known_test":
                            knowntestAnnotations.Add(annotations);
                            if (!knowntestimages.Contains(image))
                            {
                                knowntestimages.Add(image);
                            }
                            break;
                        case "transVal":
                            if (allImages.TryGetValue(annotations.image_id, out image))
                            {
                                transvalAnnotations.Add(annotations);
                                if (!transvalimages.Contains(image))
                                {
                                    transvalimages.Add(image);
                                }
                            }
                            break;
                        case "transTest":
                            if (allImages.TryGetValue(annotations.image_id, out image))
                            {
                                transtestAnnotations.Add(annotations);
                                if (!transtestimages.Contains(image))
                                {
                                    transtestimages.Add(image);
                                }
                            }
                            break;
                    }

                }
            }



            FileInfo file = new FileInfo(path);
            string outputPath = Path.Combine(file.DirectoryName, "output");
            DirectoryInfo dir = new DirectoryInfo(outputPath);
            if (!dir.Exists)
            {
                dir.Create();
            }

            deserialized.annotations = knowntrainAnnotations.ToArray();
            deserialized.images = knowntrainimages.ToArray();
            var serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            System.IO.File.WriteAllText(outputPath + @"\adv5_train.json", serialized);

            deserialized.annotations = knownvalAnnotations.ToArray();
            deserialized.images = knownvalimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            System.IO.File.WriteAllText(outputPath + @"\adv5_known_val.json", serialized);

            deserialized.annotations = knowntestAnnotations.ToArray();
            deserialized.images = knowntestimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            System.IO.File.WriteAllText(outputPath + @"\adv5_known_test.json", serialized);

            deserialized.annotations = transvalAnnotations.ToArray();
            deserialized.images = transvalimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            System.IO.File.WriteAllText(outputPath + @"\adv5_trans_val.json", serialized);

            deserialized.annotations = transtestAnnotations.ToArray();
            deserialized.images = transtestimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            System.IO.File.WriteAllText(outputPath + @"\adv5_trans_test.json", serialized);


        }
    }
}

