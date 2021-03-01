using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;

namespace DatasetHandler.COCOContext
{
    public static class CreateContextRCNN
    {
        public static IOrderedEnumerable<T> OrderByAlphaNumeric<T>(this IEnumerable<T> source, Func<T, string> selector)
        {
            int max = source
                .SelectMany(i => Regex.Matches(selector(i), @"\d+").Cast<Match>().Select(m => (int?)m.Value.Length))
                .Max() ?? 0;

            return source.OrderBy(i => Regex.Replace(selector(i), @"\d+", m => m.Value.PadLeft(max, '0')));
        }

        public static void Create()
        {
            string targetfilename = @"C:\Temp\Thesis\200826AA.TLVframes\cococamerastyle.json";
            string sourcefolder = @"C:\Temp\Thesis\200826AA.TLVframes";
            int locationId = 1;

            COCOContext.COCOForContextRCNN newdataset = new COCOContext.COCOForContextRCNN();

            newdataset.info = new Info() { contributor = "Felice Estermann", date_created = "01.03.2021", description = "BokuTimelapse", year = 2021, version = "01" };
            newdataset.licenses = new License[1];
            newdataset.licenses[0] = new License();
            newdataset.licenses[0].id = 1;
            newdataset.licenses[0].name = "LIC";

            newdataset.categories = GetCategories();



            System.IO.DirectoryInfo dirinfo = new DirectoryInfo(sourcefolder);

            DateTime startTime = DateTime.Parse("2020-08-26 05:49:58");

            var files = dirinfo.GetFiles("*.jpg");



            var sorted = files.OrderBy(item => item.Name, new NaturalStringComparer());


            int frameno = 0;

            List<Image> images = new List<Image>();


            foreach(var file in sorted)
            {
                Image img = new Image();

                DateTime date = startTime.AddSeconds(frameno * 10);
                img.date_captured = date.ToString("yyyy-MM-dd HH:mm:ss");

                img.height = 720;
                img.width = 1280;

                img.id = startTime.Year.ToString() + startTime.Month + startTime.Day + frameno.ToString("D5");

                img.location = locationId.ToString();
                img.seq_num_frames = files.Length;
                img.frame_num = frameno;
                


                img.file_name = file.Name;

                images.Add(img);
                frameno++;
            }

            newdataset.images = images.ToArray();


            newdataset.annotations = new Annotation[0];


            var serialized = JsonSerializer.Serialize(newdataset, typeof(COCOForContextRCNN));
            System.IO.File.WriteAllText(targetfilename, serialized);


        }

        private static Category[] GetCategories()
        {
            List<Category> categories = new List<Category>();

            categories.Add(new Category() { id = 0, name = "empty" });

            return categories.ToArray();
        }
    }
}
