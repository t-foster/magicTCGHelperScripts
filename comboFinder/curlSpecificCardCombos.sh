#!/bin/zsh


TODAY=`date +%Y-%m-%d`

mkdir -p specific

for (( i=1; i<=20; i++ )); do
  echo "Count: $i"
  curl -o specific/$1_$i.html "https://commanderspellbook.com/search/" -G -d "q=$1&groupByCombo=false&order=desc&page=$i"  -L

  echo "return code is $?"

  xmllint --recover specific/$1_$i.html > specific/$1_$i.recovered.html
  rm specific/$1_$i.html

  COMBO_COUNT=`grep -c comboResultSection specific/$1_$i.recovered.html`

  if [[ "$COMBO_COUNT" = "0" ]]
  then
    echo "found $i pages of combinations for $1"
    exit
  fi
done
