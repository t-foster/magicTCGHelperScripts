#!/bin/zsh

mkdir -p comboFiles
for (( i=1; i<=200; i++ )); do
  echo "Count: $i"
  curl -o comboFiles/mostpopular$i.html "https://commanderspellbook.com/search/" -G -d "sort=popularity&groupByCombo=false&order=desc&page=$i"  -L
done

for (( i=1; i<=100; i++ )); do
  echo "Count: $i"
  curl -o comboFiles/mostRecent$i.html "https://commanderspellbook.com/search/" -G -d "sort=created&groupByCombo=false&order=desc&page=$i"  -L
done

