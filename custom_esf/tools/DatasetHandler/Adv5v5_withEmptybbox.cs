using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class Adv5v5_withEmptybbox
    {
        private Coco _full;

        public Adv5v5_withEmptybbox(string full)
        {
            string jsonString = File.ReadAllText(full);
            _full = JsonSerializer.Deserialize<Coco>(jsonString);
        }

        public void AddEmptyPictures()
        {
            var emptyGetter = new EmptyImageGetter(_full);

            var emptyimages = emptyGetter.GetEmptyImages();

            List<Image> transValImages = new List<Image>();
            List<Image> transTestImages = new List<Image>();
            List<Image> knownvalImages = new List<Image>();
            List<Image> knowntrainImages = new List<Image>();
            List<Image> knowntestImages = new List<Image>();




            foreach (var image in emptyimages)
            {
                string targetfile = Adv5_DatasetHandler.GetTargetDatasetOfImage(image);

                switch(targetfile)
                {
                    case "transVal":
                        if (transValImages.Count < 170)
                        {
                            transValImages.Add(image);
                        }
                        break;
                    case "transTest":
                        transTestImages.Add(image);
                        break;
                    case "known_train":
                        knowntrainImages.Add(image);
                        break;
                    case "known_val":
                        knownvalImages.Add(image);
                        break;
                    case "known_test":
                        knowntestImages.Add(image);
                        break;
                }

            }

            string sourcePath = @"C:\Work\Github\esf-bt2020_mmdetection\customDataCaltech\adv5";
            string targetPath = @"C:\Work\Github\esf-bt2020_mmdetection\customDataCaltech\adv5v5";



            AppendImages(sourcePath, targetPath, "adv5_train.json", "adv5v5_train.json", knowntrainImages);
            AppendImages(sourcePath, targetPath, "adv5_known_val.json", "adv5v5_known_val.json", knownvalImages);
            AppendImages(sourcePath, targetPath, "adv5_known_test.json", "adv5v5_known_test.json", knowntestImages);
            
            AppendImages(sourcePath, targetPath, "adv5_trans_val.json", "adv5v5_trans_val.json", transValImages);
            AppendImages(sourcePath, targetPath, "adv5_trans_test.json", "adv5v5_trans_test.json", transTestImages);



        }

        private void AppendImages(string sourceFolder, string targetFolder, string sourceFilename, string targetFilename, List<Image> imagesToAdd)
        {
            string jsonString = File.ReadAllText(Path.Combine(sourceFolder, sourceFilename));
            var deserialized = JsonSerializer.Deserialize<Coco>(jsonString);

            var allannotations = deserialized.annotations.ToList();

            var allimages = deserialized.images.ToList();

            foreach(var newimage in imagesToAdd )
            {
                allimages.Add(newimage);

                Annotation newanno = new Annotation();
                newanno.image_id = newimage.id;
                newanno.area = 0;
                newanno.bbox = new double[4] { 0, 0, 0, 0 };
                newanno.iscrowd = 0;
                newanno.id = newanno.image_id + "empty";
                newanno.category_id = 51; //set empty bbox to 51=>fox


                allannotations.Add(newanno);
            }

            var categories = deserialized.categories.ToList();
            //categories.Add(new Category() { id = 0, name = "customEmpty", supercategory = null });
            deserialized.categories = categories.ToArray();

            deserialized.images = allimages.ToArray();
            deserialized.annotations = allannotations.ToArray();

            var serialized = JsonSerializer.Serialize(deserialized, typeof(Coco));
            System.IO.File.WriteAllText(Path.Combine(targetFolder, targetFilename), serialized);
        }
    }


}
