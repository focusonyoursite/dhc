set -e
mkdir -p out/animatie
r(){ node frames.mjs $1 $2 $3 $4 $5 fr-$6 30; ffmpeg -y -loglevel error -framerate 30 -i fr-$6/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 17 -movflags +faststart out/animatie/$6.mp4; }
r 1080 1080 staand licht .62 dhc-logo-animatie-1x1-licht &
r 1080 1080 staand donker .62 dhc-logo-animatie-1x1-donker &
wait
r 1920 1080 liggend donker .7 dhc-logo-animatie-16x9-donker &
r 1080 1920 staand donker .72 dhc-logo-animatie-9x16-donker &
wait
ffmpeg -y -loglevel error -i out/animatie/dhc-logo-animatie-1x1-licht.mp4 -vf "fps=20,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=48[p];[b][p]paletteuse" out/animatie/dhc-logo-animatie-480.gif
echo done
