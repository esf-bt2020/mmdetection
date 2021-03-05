using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace DatasetHandler
{
    public class YoloImageSeperator
    {

        public static void SeperateImagesCCTAdv5v2()
        {

            string targetfolder = @"E:\FFHS_BT\Datasets\cct_adv5v2_yolo_images";

            string knowntest = @"C:\Temp\COCO_CONVERT\cct_adv5v2\yolo_out\known_test\manifest.txt";
            SeperateImages(knowntest, Path.Combine(targetfolder, "known_test"));

            string knownval = @"C:\Temp\COCO_CONVERT\cct_adv5v2\yolo_out\known_val\manifest.txt";
            SeperateImages(knownval, Path.Combine(targetfolder, "known_val"));

            string train = @"C:\Temp\COCO_CONVERT\cct_adv5v2\yolo_out\train\manifest.txt";
            SeperateImages(train, Path.Combine(targetfolder, "train"));

            string transtest = @"C:\Temp\COCO_CONVERT\cct_adv5v2\yolo_out\trans_test\manifest.txt";
            SeperateImages(transtest, Path.Combine(targetfolder, "transtest"));


            string transval = @"C:\Temp\COCO_CONVERT\cct_adv5v2\yolo_out\transval\manifest.txt";
            SeperateImages(transval, Path.Combine(targetfolder, "transval"));
        }


        public static void SeperateImages(string manifest, string targetFolder)
        {
            string[] files = File.ReadAllLines(manifest);
            DirectoryInfo dirinfo = new DirectoryInfo(targetFolder);
            if ( !dirinfo.Exists )
            {
                dirinfo.Create();
            }
            CopyFilesToTargetFolder(files, targetFolder);
        }

        private static void CopyFilesToTargetFolder(string[] files, string targetFolder)
        {
            foreach (var file in files)
            {
                FileInfo fileinfo = new FileInfo(file);
                if (fileinfo.Exists)
                {
                    var targetfilefullname = System.IO.Path.Combine(targetFolder, fileinfo.Name);
                    fileinfo.CopyTo(targetfilefullname);
                }
                else
                {

                }
            }
        }
    }
}
