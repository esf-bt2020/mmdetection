using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class DatasetAnalyzer
    {
        public static Dictionary<long, AnimalStatistics> AnalyzeDataset(Coco dataset)
        {


            Dictionary<long, AnimalStatistics> animalStatistics = new Dictionary<long, AnimalStatistics>();

            Dictionary<string, Image> allImages = new Dictionary<string, Image>();

            foreach (var image in dataset.images)
            {
                allImages.Add(image.id, image);
            }

            foreach (var annotations in dataset.annotations)
            {
                Image image;
                if (allImages.TryGetValue(annotations.image_id, out image))
                {

                    if (animalStatistics.TryGetValue(annotations.category_id, out var stats))
                    {
                        if (stats.ImagesPerLocation.TryGetValue(image.location, out var list))
                        {
                            list.Add(image);
                        }
                        else
                        {
                            stats.ImagesPerLocation.Add(image.location, new List<Image> { image });
                        }
                    }
                    else
                    {
                        AnimalStatistics statistics = new AnimalStatistics();
                        statistics.CategoryId = annotations.category_id;
                        statistics.ImagesPerLocation = new Dictionary<string, List<Image>>();
                        statistics.ImagesPerLocation.Add(image.location, new List<Image>() { image });
                        animalStatistics.Add(annotations.category_id, statistics);
                    }

                }
            }
            return animalStatistics;
        }

        private static List<int> GetLocations(Coco dataset)
        {
            List<int> locations = new List<int>();

            foreach (var image in dataset.images)
            {
                if (!locations.Contains(int.Parse(image.location)))
                {
                    locations.Add(int.Parse(image.location));
                }
            }
            locations.Sort();
            return locations;
        }


        public static void CreateFullStatistic(string file)
        {
            string jsonString = File.ReadAllText(file);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            var stats = AnalyzeDataset(deserialized);

            var locations = GetLocations(deserialized);

            StringBuilder stringBuilder = new StringBuilder();

            string output = string.Empty;

            stringBuilder.Append("CategoryId");

            foreach (var locid in locations)
            {
                stringBuilder.Append(";" + locid);
            }
            stringBuilder.Append(Environment.NewLine);

            foreach (var key in stats.Keys)
            {
                stringBuilder.Append(key);
                if (stats.TryGetValue(key, out var stat))
                {
                    //Output category
                    foreach (var locid in locations)
                    {
                        if (stat.ImagesPerLocation.TryGetValue(locid.ToString(), out var images))
                        {
                            stringBuilder.Append(";" + images.Count);
                        }
                        else
                        {
                            stringBuilder.Append(";" + 0);
                        }
                    }
                }
                stringBuilder.Append(Environment.NewLine);
            }
            string result = stringBuilder.ToString();
        }
    }

    public class AnimalStatistics
    {
        public long CategoryId { get; set; }
        public Dictionary<string, List<Image>> ImagesPerLocation { get; set; }
    }

}
