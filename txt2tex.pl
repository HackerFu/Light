#!/usr/bin/perl
# 将txt文本转化为tex文件，实现自动排版
undef $/;

$text=<>;
$text=~s/^/\\documentclass\{ctexart\}\n\\begin\{document\}\n/g; 
$text=~s/(?<=\S)(?=$)/\n\\end\{document\}/g;
print($text);
