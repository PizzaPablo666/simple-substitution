#include <iostream>
#include <algorithm>
#include <cctype>
#include <string>
#include <sstream>
#include <fstream>
#include <unistd.h>
using namespace std;

int main(){

string key, cipher;
int i;
bool valid = false, valid_key = false, valid_cipher = false;

	// input and check key //
	while(!valid_key){
		cout <<  "Enter the key from the cipher analyses" << endl;
		cin >> key;
		if (std::all_of(begin(key), end(key), ::isalpha))
		{
		  valid_key = true;
   		   break;
		}
	}
	sleep(3);	
	while(!valid_cipher){
		cout <<  "Enter the encrypted message you were analyzing" << endl;
		cin >> cipher;
		if (std::all_of(begin(cipher), end(cipher), ::isalpha))
		{
		  valid_cipher = true;
   		   break;
		}
	}

	
	//appending//
	string check = "";
	check += key;
	check += "|";
	check += cipher;

	//checking the cypher and key//
	ifstream inFile;
	string line;
	bool valid_pair = false;

	inFile.open("pairs");

	while (getline(inFile,line))
	{
		if(line == check){
			valid_pair = true;
			cout << " YEY " << endl;
		}

	}












return 0;
}
