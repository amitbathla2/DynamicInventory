python ec2.py > test
sed -i 's/None/Linux/g' test
grep "Linux" test> Linux_Host
grep "windows" test> Windows_Host
echo "[Linux]" > Final_Inventory
cat Linux_Host|awk '{print $1}'>> Final_Inventory
echo "[Windows]" >> Final_Inventory
cat Windows_Host|awk '{print $1}'>> Final_Inventory
