I was going to try running [PilOS](http://picolisp.com/wiki/?PilOS) in QEMU as shown on its wiki page. The wiki says:

>You can download a tarball with all sources, and a ready-made image to be put onto an USB-Stick or passed to Qemu.

>     $ wget http://software-lab.de/pilos.tgz
    $ tar xvfz pilos.tgz
    $ cd pilos
>You can now start it with Qemu:

>     $ qemu-system-x86_64  -m 4096  -ctrl-grab  -no-reboot  x86-64.img

I did this, but when I ran the last command I got a screen like:

[![enter image description here][1]][1]

That's okay, maybe there's a bug in PilOS; **I am not asking for support on PilOS specifically**. <br> However, QEMU complained:

    WARNING: Image format was not specified for 'x86-64.img' and probing guessed raw.
             Automatically detecting the format is dangerous for raw images, write operations on block 0 will be restricted.
             Specify the 'raw' format explicitly to remove the restrictions.

I googled around a little and found the (seemingly) applicable command-line argument on the [QEMU Wiki](http://wiki.qemu.org/download/qemu-doc.html):

>Supported image file formats:

> **‘raw’**: Raw disk image format (default). This format has the advantage of being simple and easily exportable to all other emulators. If your file system supports holes (for example in ext2 or ext3 on Linux or NTFS on Windows), then only the written sectors will reserve space. Use qemu-img info to know the real size used by the image or ls -ls on Unix/Linux.

So, I ran:

    $ qemu-system-x86_64  -m 4096  -ctrl-grab  -no-reboot  x86-64.img  raw

Which gave:

    WARNING: Image format was not specified for 'x86-64.img' and probing guessed raw.
             Automatically detecting the format is dangerous for raw images, write operations on block 0 will be restricted.
             Specify the 'raw' format explicitly to remove the restrictions.
    qemu-system-x86_64: -no-reboot: drive with bus=0, unit=0 (index=0) exists

QEMU does not load, just exits with `$?` set.

1. How do I properly specify the `raw` format to QEMU?

2. Does `drive with bus... exists` mean it can't mount PilOS on `bus 0` because that's where `/dev/sda`, my boot drive, is located?

3. Assuming the `READ ERROR 09` is because of my lack of experience with QEMU and not a bug in PilOS, what else can I do to make it load properly? (It should give a white-on-blue terminal prompt, waiting for LISP code, like on the Wiki linked above.)

  [1]: http://i.stack.imgur.com/AqpeF.png
