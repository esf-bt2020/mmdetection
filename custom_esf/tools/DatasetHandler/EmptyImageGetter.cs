using System;
using System.Collections.Generic;
using System.Text;

namespace DatasetHandler
{
    public class EmptyImageGetter
    {
        private Coco _Dataset { get; set; }

        public EmptyImageGetter(Coco dataset)
        {
            this._Dataset = dataset;
        }

        private List<Annotation> GetAnnotationsOfByImageId(string imageid)
        {
            List<Annotation> annotations = new List<Annotation>();
            foreach (var annot in _Dataset.annotations )
            {
                if ( annot.image_id == imageid)
                {
                    annotations.Add(annot);
                }
            }
            return annotations;
        }

        public List<Image> GetEmptyImages()
        {
            List<Image> images = new List<Image>();

            List<Image> imagesid30 = new List<Image>();

            foreach (var image in this._Dataset.images )
            {
                var annotations = GetAnnotationsOfByImageId(image.id);
                if ( annotations.Count < 1 )
                {
                    images.Add(image);
                }
            }
            return images;
        }
    }
}
