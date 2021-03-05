using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class CCTAnalyzerSpecialPicturesWithoutbbox
    {
        private string _Filename = null;
        private COCOCCT.COCOCCT _COCO;

        public CCTAnalyzerSpecialPicturesWithoutbbox(string filename)
        {
            _Filename = filename;
            string jsonString = File.ReadAllText(Path.Combine(_Filename));
            _COCO = JsonSerializer.Deserialize<COCOCCT.COCOCCT>(jsonString);
        }

        public List<string> GetImageIdsOfEmptyPictures()
        {
            var list = PicturesOfCategory(30);
            return list;
        }

        public List<string> GetImageIdsOfCars()
        {
            var list = PicturesOfCategory(33);
            return list;
        }

        private COCOCCT.Image GetImageByImageId(string imageId)
        {
            foreach (var img in _COCO.images)
            {
                if (img.id == imageId)
                {
                    return img;
                }
            }
            return null;
        }

        public void CopyImagesOfCategoryToAnotherFolder(string sourcefolder, string targetfolder, int categoryId)
        {
            var imageids = PicturesOfCategory(categoryId);

            int imagenotfoundcounter = 0;


            foreach (var imageId in imageids)
            {

                var image = GetImageByImageId(imageId);
                if ( image == null )
                {
                    imagenotfoundcounter++;
                    Console.WriteLine("Image not found!");
                    continue;
                }

                string sourceFilename = Path.Combine(sourcefolder, image.file_name);
                string destinationFilename = Path.Combine(targetfolder, image.file_name);

                FileInfo file = new FileInfo(sourceFilename);
                if (file.Exists)
                {
                    file.CopyTo(destinationFilename);
                }
            }
        }

        public List<string> PicturesOfCategory(int categoryId)
        {
        

           
            List<string> images = new List<string>();
            int imagesWithbbox = 0;
            foreach(var ann in _COCO.annotations)
            {
                if ( ann.category_id == categoryId )
                {
                    if (ann.bbox == null)
                    {
                        images.Add(ann.image_id);
                    }
                    else
                    {
                        imagesWithbbox++;
                    }
                }
            }
            return images;

        }
    }
}
