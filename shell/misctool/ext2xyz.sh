find mouse/**/* -depth -name "*.mou.m02" -exec sh -c 'mv "$1" "${1%.mou.m02}.m02"' _ {} \;
