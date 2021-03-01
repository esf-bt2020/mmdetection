using System;
using System.Collections.Generic;
using System.Text;

namespace DatasetHandler
{
    public class Advx_DatasetHandler
    {
        public long CategoryId { get; set; }
        public Dictionary<string, List<ImageDescription>> ImagesPerLocation { get; set; }

        private static List<long> _CategoriesToUse = new List<long>() { 3, 5, 6, 8, 9, 10, 11, 16, 34, 51 }; //10 Classes

        public static bool IsAnimalRelevant(long categoryId)
        {
            return _CategoriesToUse.Contains(categoryId);
        }

        private static List<long> _LocationsValTrans = new List<long>() { 32, 42, 56, 64, 65, 66, 90, 100, 108, 115, 120 }; //11 Val Trans Location
        private const int maxValPerLocation = 150;
        private const int maxValTotal = 300;

        private static List<long> _LocationsTestTrans = new List<long>() { 16, 28, 39, 59, 60, 63, 72, 78 }; //8 Test Trans Location
        private int maxTestPerLocation = 100;
        private int maxTestTotal = 200;

        private const int maxTrainPerLocation = 200;
        private const int maxTrainTotal = 1000;

        public int GetImagesOfTypeInLocation(string location, string type)
        {
            int imagesOfTypeInLocation = 0;
            if (ImagesPerLocation.TryGetValue(location, out var list))
            {
                int counter = 0;
                foreach (ImageDescription img in list)
                {
                    if (img.type == type)
                    {
                        counter++;
                    }
                }
                imagesOfTypeInLocation = counter;
            }
            return imagesOfTypeInLocation;
        }

        public int GetImagesOfTypeInAllLocation(string type)
        {
            int counter = 0;
            foreach (var key in ImagesPerLocation.Keys)
            {
                if (ImagesPerLocation.TryGetValue(key, out var list))
                {
                    foreach (ImageDescription img in list)
                    {
                        if (img.type == type)
                        {
                            counter++;
                        }
                    }
                }
            }
            return counter;
        }

        public bool IsLimitReached(Image image, string type)
        {

            int imagesOfTypeInLocation = GetImagesOfTypeInLocation(image.location, type);
            int imagesOfCategory = GetImagesOfTypeInAllLocation(type);

            switch (type)
            {
                case "transVal":
                    if (imagesOfTypeInLocation >= maxValPerLocation)
                    {
                        return true;
                    }
                    else if (imagesOfCategory >= maxValTotal)
                    {
                        return true;
                    }
                    break;
                case "transTest":
                    if (imagesOfTypeInLocation >= maxTestPerLocation)
                    {
                        return true;
                    }
                    else if (imagesOfCategory >= maxTestTotal)
                    {
                        return true;
                    }
                    break;
                case "known_train":
                    if (imagesOfTypeInLocation >= maxTrainPerLocation)
                    {
                        return true;
                    }
                    else if (imagesOfCategory >= maxTrainTotal)
                    {
                        return true;
                    }
                    break;
                case "known_val":
                    if (imagesOfTypeInLocation >= maxValPerLocation)
                    {
                        return true;
                    }
                    else if (imagesOfCategory >= maxValTotal)
                    {
                        return true;
                    }
                    break;
                case "known_test":
                    if (imagesOfTypeInLocation >= maxTestPerLocation)
                    {
                        return true;
                    }
                    else if (imagesOfCategory >= maxTestTotal)
                    {
                        return true;
                    }
                    break;
            }
            return false;
        }

        public static string GetTargetDatasetOfImage(Image image)
        {
            if (_LocationsValTrans.Contains(long.Parse(image.location)))
            {
                return "transVal";
            }
            else if (_LocationsTestTrans.Contains(long.Parse(image.location)))
            {
                return "transTest";
            }
            DateTime date = DateTime.Parse(image.date_captured);

            int mod = date.DayOfYear % 10;

            if (mod < 7)
            {
                return "known_train";
            }
            else if (mod < 9)
            {
                return "known_val";
            }
            else if (mod < 10)
            {
                return "known_test";
            }
            else
            {
                throw new Exception("Invalid modulo!");
            }
        }
    }

    //public class ImageDescription
    //{
    //    public string type { get; set; }
    //    public Image image { get; set; }
    //}
}
