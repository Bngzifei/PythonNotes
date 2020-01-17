## HttpImageFilter

这个模块用来分发JPEG，GIF和PNG图片。这个没有默认开启，在编译nginx中通过./configure参数配置。

```nginx
--with-http_image_filter_module  
```

编译和运行这个模块必须安装libgd库。我们推荐使用最新版本的Libgd。

示例:

```nginx
ocation /img/ {
    proxy_pass     http://backend;
    image_filter   resize  150 100;
    error_page     415   = /empty;

}
 
location = /empty {
    empty_gif;
}
```

### image_filter

```nginx
Syntax: image_filter (test|size|resize width height|crop width height)

Default: none

Context: location

Specifies the type of transformation to apply to the image, one of the below:
详细的图片后缀类型如下：

test: checking that the response is indeed an image format JPEG, GIF or PNG. Otherwise, an error 415.
测试：测试确定图片文件的后缀格式为JPEG，GIF OR PNG。否则返回415错误
size: Gives information about the image in JSON format. For example,
尺寸：返回JSON格式的图片信息。例如：
{ "img" : { "width": 100, "height": 100, "type": "gif" } }
Or if an error occurs,
或者如果发生错误,

{}
resize: proportionally reduces the image to a specified size.
调整大小：缩略图片到特定的尺寸
crop: proportionally reduces the image to a specified size and trims extra edge.
切割：切割图片到特定的尺寸和特定的分辨率
```

### image_filter_buffer

```nginx
Syntax: image_filter_buffer size

Default: 1M

Context: http, server, location

Sets the maximum size for reading the image.
设置读取文件的最大的尺寸
```

### image_filter_jpeg_quality

```nginx
Syntax: image_filter_jpeg_quality [0...100]

Default: 75

Context: http, server, location

Sets the rate of loss of information when processing the images as JPEG. The maximum recommended value is 95.
设置处理JPEG图片的丢失信息率.推荐的最大值为95
```

### image_filter_transparency

```nginx
Syntax: image_filter_transparency on|off

Default: on

Context: http, server, location

This directive allows you to disable image transparency in GIF and palette-based PNG to improve image resampling quality.
这个指令容许你关闭GIF图片的透明度和 PNG图片质量

True color PNG alpha-channels are always preserved despite this setting.
真彩色PNG图片保存忽略设定

Note: Grayscale PNG's are untested, but should be handled as truecolor PNGs.
注释：灰度PNG图片未被设置，但应该被作为真彩色PNG图片处理
```

