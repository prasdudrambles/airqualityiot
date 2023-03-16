#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>


using namespace std;


string prasdud(string str){
	string tempstr="";
	reverse(str.begin(),str.end());
	cout<<str;
	return str;

}

int main(){
	prasdud("codewars");
	return 1;
}
