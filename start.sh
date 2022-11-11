if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Emilyoftg/Nathalia2 /Nathalia2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Nathalia2
fi
cd /Nathalia2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
