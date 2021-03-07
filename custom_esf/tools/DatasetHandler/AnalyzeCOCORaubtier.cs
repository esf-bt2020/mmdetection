using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;

namespace DatasetHandler
{
    public class AnalyzeCOCORaubtier
    {
        public static void AnalyzeDataset()
        {
            string train = @"C:\Data\FFHS\BT\raubtierv2_b\train\_annotations.coco.json";
            string valid = @"C:\Data\FFHS\BT\raubtierv2_b\valid\_annotations.coco.json";
            string test = @"C:\Data\FFHS\BT\raubtierv2_b\test\_annotations.coco.json";
            CreateFullStatistic(train);
            CreateFullStatistic(valid);
            CreateFullStatistic(test);

        }
        public static void CreateFullStatistic(string file)
        {
            string jsonString = File.ReadAllText(file);
            var deserialized = JsonSerializer.Deserialize<COCORaubtierV2.COCORaubtierV2>(jsonString);


            StringBuilder stringBuilder = new StringBuilder();
            int imgwithbbox = 0;

            int cat1annocounter = 0;
            int cat2annocounter = 0;
            int cat3annocounter =0;

            int cat1imgcounter = 0;
            int cat2imgcounter = 0;
            int cat3imgcounter = 0;

            foreach (var image in deserialized.images )
            {
                int annoCounter = 0;
                long? category = null;
                foreach(var anno in deserialized.annotations )
                {
                    if ( anno.image_id == image.id )
                    {
                        annoCounter++;
                        switch(anno.category_id )
                        {
                            case 1:
                                cat1annocounter++;
                                break;
                            case 2:
                                cat2annocounter++;
                                break;
                            case 3:
                                cat3annocounter++;
                                break;
                        }
                        if ( category == null )
                        {
                            category = anno.category_id;
                            switch (category)
                            {
                                case 1:
                                    cat1imgcounter++;
                                    break;
                                case 2:
                                    cat2imgcounter++;
                                    break;
                                case 3:
                                    cat3imgcounter++;
                                    break;
                            }
                        }
                        else
                        {
                            if (category != anno.category_id)
                            {
                                Console.WriteLine("Fehler!");
                            }
                        }
                    }
                }
                if (annoCounter > 0 )
                {
                    imgwithbbox++;
                }
            }

            string output = string.Empty;

            stringBuilder.Append("CategoryId");


            string result = stringBuilder.ToString();
        }
    }

}
