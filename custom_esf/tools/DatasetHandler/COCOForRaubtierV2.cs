using System;
using System.Collections.Generic;
using System.Globalization;

namespace DatasetHandler.COCORaubtierV2
    {


        public partial class COCORaubtierV2
        {
            public Info info { get; set; }


            public License[] licenses { get; set; }


            public Category[] categories { get; set; }


            public Image[] images { get; set; }


            public Annotation[] annotations { get; set; }
        }

        public partial class Annotation
        {

            public long id { get; set; }

            public string id_caltech { get; set; }


            public long image_id { get; set; }

            public string image_id_caltech { get; set; }


            public long category_id { get; set; }


            public double[] bbox { get; set; }


            public double area { get; set; }


            public object[] segmentation { get; set; }


            public long iscrowd { get; set; }
        }

        public partial class Category
        {

            public long id { get; set; }

            public string name { get; set; }

            public string supercategory { get; set; }
        }

        public partial class Image
        {
            public long id { get; set; }

            public string id_caltech { get; set; }

            public long license { get; set; }

            public string file_name { get; set; }


            public long height { get; set; }

            public long width { get; set; }

            public string date_captured { get; set; }

            //Added Properties
            public string location { get; set; } //je nach File  string oder long
            public long seq_num_frames { get; set; }
            public long frame_num { get; set; }

            public string seq_id { get; set; }
        }

        public partial class Info
        {

            public string year { get; set; }


            public string version { get; set; }

            public string description { get; set; }

            public string contributor { get; set; }

            public Uri url { get; set; }

            public string date_created { get; set; }
        }

        public partial class License
        {
            public long id { get; set; }

            public string url { get; set; }

            public string name { get; set; }
        }
    }



