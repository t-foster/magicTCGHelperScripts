#!/bin/zsh


TODAY=`date +%Y-%m-%d`

mkdir -p recent

for (( i=1; i<=100; i++ )); do
  echo "Count: $i"
  curl -o recent/mostRecent$TODAY-$i.html  "https://commanderspellbook.com/search/" -G -d "sort=created&groupByCombo=false&order=desc&page=$i"  -L

  xmllint --recover recent/mostRecent$TODAY-$i.html > recent/mostRecent$TODAY-$i.recovered.html
  rm recent/mostRecent$TODAY-$i.html
done

