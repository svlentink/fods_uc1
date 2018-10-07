#!/bin/bash

[[ -z $1 ]] && echo "Usage: $0 /location/to/data" && exit 1
DIR="$1"
[[ $2 == '-i' ]] && INTERACTIVE=1


getListOfSuspectedWords() {
  for file in `find $DIR -name '*.tex'`
  do
    cat $file
  done | aspell list -t | sort | uniq
}

loopOverWords() {
  echo Entering $FUNCNAME
  for word in `getListOfSuspectedWords`
  do
    echo $word
    if [[ $INTERACTIVE == 1 ]]
    then
      processWord $word
    fi
  done
}

processWord() {
  local word=$1
  read -n 1 -p "[l]ist/[c]hange occurences or press enter to skip" answr
  case $answr in
		[Cc]* ) changeWord $word;;
		[Ll]* ) grep -ri $word $DIR && processWord $word;;
		* ) echo 'okay, skipping it';;
	esac
}

changeWord() {
  local word=$1
  read -p "Change $word into : " newword
  for file in `find $DIR -name '*.tex'`
  do
    sed -i "s/$word/$newword/g" $file
  done
  echo Changed $word into $newword
}

extraLinebreaks() {
  for tex in `find $DIR -name "*.tex"`
  do
    sed -i 's/\.\ /.\n/g' $tex
    sed -i 's/,\ /,\n/g' $tex
    sed -i 's/“/"/g' $tex
    sed -i 's/”/"/g' $tex
    sed -i "s/‘/'/g" $tex
    sed -i "s/’/'/g" $tex
  done
}

loopOverWords
