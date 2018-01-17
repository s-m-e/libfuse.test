# How to use

1. Compile the code and set the stage:
   ```./build.sh```

2. Mount filesystem in one shell with
   ```./hello_{API}_{N}.bin -f mnt```
   where {N} is either 2 or 3 (versions if libfuse).
   Filesystem will print to stderr.

3. Run tests in another shell with
   ```python3 call.py```

# Relevant results for high level API

![screen shot](screenshot01.png "screen shot")
