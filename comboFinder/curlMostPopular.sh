#!/bin/zsh


TODAY=`date +%Y-%m-%d`

mkdir -p popular
for (( i=1; i<=200; i++ )); do
  echo "Count: $i"
  curl -o popular/mostpopular$TODAY-$i.html "https://commanderspellbook.com/search/" -G -d "sort=popularity&groupByCombo=false&order=desc&page=$i"  -L

  xmllint --recover popular/mostpopular$TODAY-$i.html > popular/mostpopular$TODAY-$i.recovered.html
  rm popular/mostpopular$TODAY-$i.html
done

