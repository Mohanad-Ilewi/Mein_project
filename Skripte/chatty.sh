#!/bin/bash

# Willkommen Chatty

echo "Hallo, ich bin Chatty. Wie heißt du?"

read name

# abfrage das Alter
echo "wie alt bist du?"
read age

# “zielgruppenorientierte” Begrüßung. Unterscheide zwischen
if [ "$age" -lt 20 ]; then
echo "Hallo $name, du bist noch jungemann."

elif [ "$age" -ge 20 ] && [ "$age" -lt 50 ]; then

echo "Hallo $name, schön dich zu sehen,"

else
echo "Hallo $name, es wäre sehr gut, ob das funktioniert."

fi

  # die nächste Fragen
echo "wo wohnst du?"
read City

echo "was ist dein lieblingsfilm?"
read Lieblingsfilm

# OPTIONAL HERAUSFORDERUNG
echo "wie gehts dir heute?"
read Gefeuhl

if [ "Gesundheit" == "gut" ]; then
echo "schoen, dich wieder hier zu sehen"

else
echo "ich wuensche dir, Gute Besserung"

fi

# Auf Wiedersehen Chatty & alle  eingegebene Infos
echo "Vielen dank Chatt, dass wir schoene zeit zusammen verbracht haben"

echo "Name: $name"
echo "Alter: $age"
echo "City: $city"
echo "Liblingsfilm: $lieblingsfilm"

fi
