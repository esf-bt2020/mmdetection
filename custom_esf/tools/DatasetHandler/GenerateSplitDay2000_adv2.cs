using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class GenerateSplitDay2000_adv2
    {

        //14 classes
        private static List<long> _CategoriesToUse = new List<long>() { 1, 3, 5, 6, 8, 9, 10, 11, 16, 33, 34, 51 };

        private static Dictionary<long, List<string>> AnnotationsPerCategory = new Dictionary<long, List<string>>();

        private const int _MaxImagesPerCategory = 2000;

        /*
         * Alle Bounding boxen der Typen einlesen inkl. image_id
         * Bounding boxen aufteilen in: tag of jahr modulo 10, 0-6 = train, 7-8 = val, 9=test
         */

        private static string GetTargetDatasetOfImage(Image image)
        {
            DateTime date = DateTime.Parse(image.date_captured);

            int mod = date.DayOfYear % 10;

            if (mod < 7)
            {
                return "train";
            }
            else if (mod < 9)
            {
                return "val";
            }
            else if (mod < 10)
            {
                return "test";
            }
            else
            {
                throw new Exception("Invalid modulo!");
            }
        }

        public static void SplitAnnotationFile(string path)
        {

            List<Annotation> trainAnnotations = new List<Annotation>();
            List<Annotation> valAnnotations = new List<Annotation>();
            List<Annotation> testAnnotations = new List<Annotation>();


            List<Image> trainimages = new List<Image>();
            List<Image> valimages = new List<Image>();
            List<Image> testimages = new List<Image>();


            string jsonString = File.ReadAllText(path);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            Dictionary<string, Image> allImages = new Dictionary<string, Image>();

            foreach (var image in deserialized.images)
            {
                allImages.Add(image.id, image);
            }


            int usedAnnotations = 0;
            int ignoredAnnotationCategory = 0;
            int ignoredAnnotationCount = 0;
            foreach (var annotations in deserialized.annotations)
            {

                if (!_CategoriesToUse.Contains(annotations.category_id))
                {
                    //Annotation nicht relevant für dataset
                    ignoredAnnotationCategory++;
                    continue;
                }

                if (AnnotationsPerCategory.TryGetValue(annotations.category_id, out var list))
                {
                    if (list.Count >= _MaxImagesPerCategory)
                    {
                        ignoredAnnotationCount++;
                        continue;
                    }
                    list.Add(annotations.id);
                }
                else
                {
                    AnnotationsPerCategory.Add(annotations.category_id, new List<string>() { annotations.id });
                }

                usedAnnotations++;

                Image image = null;
                if (allImages.TryGetValue(annotations.image_id, out image))
                {

                    string type = GetTargetDatasetOfImage(image);

                    switch (type)
                    {
                        case "train":

                            trainAnnotations.Add(annotations);
                            if (!trainimages.Contains(image))
                            {
                                trainimages.Add(image);
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
                        case "test":
                            if (allImages.TryGetValue(annotations.image_id, out image))
                            {
                                testAnnotations.Add(annotations);
                                if (!testimages.Contains(image))
                                {
                                    testimages.Add(image);
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

            deserialized.annotations = trainAnnotations.ToArray();
            deserialized.images = trainimages.ToArray();
            var serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));

            //var statstrain = GetCategoryCounterOfAnnotations(deserialized.annotations, "train");

            System.IO.File.WriteAllText(outputPath + @"\adv2_2000pcat_day_train.json", serialized);

            deserialized.annotations = valAnnotations.ToArray();
            deserialized.images = valimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            //var stats_val = GetCategoryCounterOfAnnotations(deserialized.annotations, "val");
            System.IO.File.WriteAllText(outputPath + @"\adv2_2000pcat_day_val.json", serialized);

            deserialized.annotations = testAnnotations.ToArray();
            deserialized.images = testimages.ToArray();
            serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            //var statseccvtrain = GetCategoryCounterOfAnnotations(deserialized.annotations, "eccv_train");
            System.IO.File.WriteAllText(outputPath + @"\adv2_2000pcat_day_test.json", serialized);


        }
    }
}
