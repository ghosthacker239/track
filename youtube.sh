views=1

crome https://www.youtube.com/watch?v=0j1sxARMhn8&t=17s

until [ $views -gt 10 ]

do

xdotool --window key ctrl+r

sleep 5s

((views++))

done

echo All done
