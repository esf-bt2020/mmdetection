using System;
using System.Collections.Generic;
using System.Text;

namespace DatasetHandler
{
    public class DatasetHandler
    {
        private static int _ImageIdCounter = 1;
        private static int _AnnotationIdCounter = 1;
        private static object _lockObject = new object();

        private static Dictionary<string, int> _mappingOriginalImageIdToCOCOConformId = new Dictionary<string, int>();
        private static Dictionary<string, int> _mappingOriginalAnnotationIdToCOCOConformId = new Dictionary<string, int>();

        public static int GetCOCOMappedImageId(string caltechId)
        {
            lock (_lockObject)
            {
                if (_mappingOriginalImageIdToCOCOConformId.ContainsKey(caltechId))
                {
                    if (_mappingOriginalImageIdToCOCOConformId.TryGetValue(caltechId, out var cocoId))
                    {
                        return cocoId;
                    }
                    else
                    {
                        throw new Exception("Mapping Id not found!");
                    }
                }
                else
                {
                    var counter =_ImageIdCounter++;
                    _mappingOriginalImageIdToCOCOConformId.Add(caltechId, counter);
                    return counter;
                }
            }
        }

        public static int GetCOCOMappedAnnotationId(string caltechId)
        {
            lock (_lockObject)
            {
                if (_mappingOriginalAnnotationIdToCOCOConformId.ContainsKey(caltechId))
                {
                    if (_mappingOriginalAnnotationIdToCOCOConformId.TryGetValue(caltechId, out var cocoId))
                    {
                        return cocoId;
                    }
                    else
                    {
                        throw new Exception("Mapping Id not found!");
                    }
                }
                else
                {
                    var counter = _AnnotationIdCounter++;
                    _mappingOriginalAnnotationIdToCOCOConformId.Add(caltechId, counter);
                    return counter;
                }
            }
        }
    }
}
