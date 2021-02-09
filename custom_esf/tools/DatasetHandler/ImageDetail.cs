using System;
using System.Collections.Generic;
using System.Text;

namespace DatasetHandler
{
    public class ImageDetail
    {
        public string CaltechImageId { get; set; }
        public string CocoConformId { get; set; }
        public List<string> TargetDatasets { get; set; }
    }
}
