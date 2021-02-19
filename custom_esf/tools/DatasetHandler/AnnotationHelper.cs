using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class AnnotationHelper
    {

        public static Dictionary<long, List<string>> GetImagesPerCategory(string filename)
        {

            Dictionary<long, List<string>> dicsCounter = new Dictionary<long, List<string>>();

            string jsonString = File.ReadAllText(filename);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);
            

            foreach (var annotations in deserialized.annotations)
            {
                if (dicsCounter.TryGetValue(annotations.category_id, out var list))
                {
                    list.Add(annotations.image_id_caltech);
                }
                else
                {
                    dicsCounter.Add(annotations.category_id, new List<string>() { annotations.image_id_caltech });
                }
            }
            return dicsCounter;
        }

        public static Dictionary<long, string> GetCategoryDic(string filename)
        {
            Dictionary<long, string> categories = new Dictionary<long, string>();

            string jsonString = File.ReadAllText(filename);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            foreach(var category in deserialized.categories )
            {
                categories.Add(category.id, category.name);
            }
            return categories;
        }
    }
}
