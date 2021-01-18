using System;
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
            Console.WriteLine("Hello World!");

            Parse2(@"C:\Users\faesterm\switchdrive\FFHS_aktuell\BT_Thesis\_LinuxTraining202012\caltech_bboxes_20200316_work.json");
        }

        private static void Parse2(string path)
        {
           

            string jsonString = File.ReadAllText(path);
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            foreach(var annotations in deserialized.annotations )
            {
                var arearaw = (float.Parse(annotations.bbox[2].ToString()) * float.Parse(annotations.bbox[3].ToString()));
                var area = Math.Round(arearaw, 0);
                annotations.iscrowd = 0;
                annotations.area = area;
                annotations.segmentation = new string[0];

            }

            var serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));


            System.IO.File.WriteAllText(path + "output", serialized);

           


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
