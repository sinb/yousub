# yousub
A python CLI tool to download subtitles from YouTube

## install
```
python setup.py install
```
## usage
```
# show all available subtitle languages, --show|-s
yousub --show https://www.youtube.com/watch?v=WBqnzn77MEE
# download a specified language, if -lang|-l not specified, download them all
yousub -lang en https://www.youtube.com/watch?v=WBqnzn77MEE
# -d|--directory to set output directory, -f|--filetype to set output format[xml, json, srt(default)]
# example: download json format Chinese subtitle from a url, and put it into 'subtitle' directory
yousub -l zh-CN -d subtitle -f json https://www.youtube.com/watch?v=WBqnzn77MEE
```
## help
```
yousub --help
```
