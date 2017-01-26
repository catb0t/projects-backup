#include <map>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <iostream>

typedef unsigned long long	u64;
typedef unsigned char		byte;

class interpreter {
public:
	void run( std::string c ) {
		std::istringstream is( c );
		std::copy( std::istream_iterator<std::string>( is ), std::istream_iterator<std::string>(), std::back_inserter<std::vector<std::string> >( code ) );
		codeLen = code.size(); if( !codeLen ) return;
		for( size_t i = 0; i < codeLen; i++ )
			if( code[i][0] == '>' )
				jumpTable.insert( std::make_pair( code[i].substr( 1 ), i ) );
		run();
	}
private:
	void run() {
		stack.clear(); codePtr = 0; carry = false;
		do {
			switch( tolower( code[codePtr][0] ) ) {
				case 'p': pop();			break;
				case 'j': jump();			break;
				case 'm': math();			break;
				case 'h': push();			break;
				case 'r': roll();			break;
				case 'i': input();			break;
				case 'o': output();			break;
				case 't': copy_to_tail();
			}
		} while( ++codePtr < codeLen );
	}
	void copy_to_tail() {
		if( !stack.size() ) return;
		u64 i = stack.back();
		stack.insert( stack.begin(), i );
	}
	void roll() { 
		if( !stack.size() ) return;
		stack.push_back( ( u64 )*stack.begin() );
		stack.erase( stack.begin() );
	}
	void jump() {
		if( code[codePtr].length() < 3 || !stack.size() ) return;
		switch( code[codePtr][1] ) {
			case 'n': if( !stack.back() ) return; else break;
			case 'z': if( stack.back() ) return;
		}
		std::string s = code[codePtr].substr( 2 );
		codePtr = jumpTable.find( s ) != jumpTable.end() ? jumpTable[s] : codeLen;
	}
	void math() {
		if( code[codePtr].length() < 2 ) return;
		u64 a = pop(), b = pop(), c;
		switch( code[codePtr][1] ) {
			case 'a': c = a + b; carry = c < a; break;
			case 's': c = a - b; carry = c > a;
		}
		stack.push_back( c );
	}
	void input() {
		if( code[codePtr].length() < 2 ) return;
		switch( code[codePtr][1] ) {
			case '#': 
				u64 a; std::cin >> a;
				stack.push_back( a );
				break;
			case '$':
				byte i; std::cin >> i;
				stack.push_back( static_cast<u64>( i ) );
				std::cin.ignore( 1024, '\n' );
		}
	}
	void output() {
		if( code[codePtr].length() < 2 || !stack.size() ) return;
		switch( code[codePtr][1] ) {
			case '#': std::cout << stack.back(); break;
			case '$': std::cout << static_cast<byte>( stack.back() );
		}
	}
	void push() {
		if( code[codePtr][1] == '?' ) { stack.push_back( carry ? 1 : 0 ); return; }
		if( code[codePtr].length() < 3 ) return;
		switch( code[codePtr][1] ) {
			case '#': {
				std::stringstream s( code[codePtr].substr( 2 ) );
				u64 a; s >> a;
				stack.push_back( a );
			} break;
			case '$': stack.push_back( static_cast<u64>( code[codePtr][2] ) );
		}
	}
	u64 pop() {
		if( !stack.size() ) return 0;
		u64 i = stack.back(); stack.pop_back(); return i;
	}
	std::vector<std::string> code;
	std::vector<u64> stack;
	std::map<std::string, size_t> jumpTable;
	size_t codePtr, codeLen; bool carry;
};
std::string openFile( std::string filename ) {
	std::string line, str;
	std::ifstream in( filename.c_str() );
	if( in.good() ) {
		while( std::getline( in, line ) ) {
			for( std::string::iterator g = line.begin(); g != line.end(); g++ ) {
				if( *g == ';' ) break;
				isspace( *g ) ? str.append( 1, '\n' ) : str.append( 1, *g );
			}
			str.append( 1, '\n' );
		}
		in.close();
	}
	else std::cout << "Cannot open file <" << filename << ">\n";
	return str;
}
int main( int argc, char* argv[] ) {
	if( argc < 2 ) std::cout << "Usage: xEec <filename>\n";
	else {
		interpreter i;
		i.run( openFile( argv[1] ) );
	}
	std::cout << "\n\n";
	return 0;
}