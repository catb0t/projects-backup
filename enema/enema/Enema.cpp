/*
 * Enema.cpp	$Revision: 1.3 $	$Date: 2002/11/10 16:13:55 $	MB
 */

#include <stdio.h>
#include <memory.h>
#include <string>
#include "Enema.h"

CEnema::CEnema(int memSize) : m_memSize(0), m_memory(NULL), m_programEnd(0)
{
	m_memory	= new int[memSize];
	m_memSize	= memSize;

	reset();
}

CEnema::~CEnema()
{
	if (m_memory != NULL) {
		delete [] m_memory;
		m_memory	= NULL;
	}
}

void CEnema::reset()
{
	memset(m_memory, 0, m_memSize * sizeof(int));
	memset(m_program, 0, sizeof(m_program));
	memset(m_words, 0, sizeof(m_words));

	m_pc	= 0;
}

void CEnema::run()
{
	while (true) {
		__uint_8	ch;
		int			arg1, arg2;
		__uint_8	code	= m_program[m_pc++];

		//fputc(code, stdout);
		//fputc('\n', stdout);

		if (m_words[code] == 0) {
			switch (code) {
				case '0':
				case '1':
				case '2':
				case '3':
				case '4':
				case '5':
				case '6':
				case '7':
				case '8':
				case '9':
					m_opStack.push(code - '0');
					break;

				case '+':
					arg2	= m_opStack.pop();
					arg1	= m_opStack.pop();
					m_opStack.push(arg1 + arg2);
					break;

				case '-':
					arg2	= m_opStack.pop();
					arg1	= m_opStack.pop();
					m_opStack.push(arg1 - arg2);
					break;

				case '*':
					arg2	= m_opStack.pop();
					arg1	= m_opStack.pop();
					m_opStack.push(arg1 * arg2);
					break;

				case '/':
					arg2	= m_opStack.pop();
					arg1	= m_opStack.pop();
					m_opStack.push(arg1 / arg2);
					break;

				case '%':
					arg2	= m_opStack.pop();
					arg1	= m_opStack.pop();
					m_opStack.push(arg1 % arg2);
					break;

				case 'D':
					m_opStack.dup();
					break;

				case 'X':
					m_opStack.drop();
					break;

				case 'S':
					m_opStack.swap();
					break;

				case 'R':
					m_opStack.rot();
					break;

				case 'G':
					arg1	= m_opStack.pop();
					m_opStack.push(m_memory[arg1 % m_memSize]);
					break;

				case 'P':
					arg2	= m_opStack.pop();
					arg1	= m_opStack.pop();
					m_memory[arg1 % m_memSize]	= arg2;
					break;

				case 'I':
					m_opStack.push(fgetc(stdin));
					break;

				case 'O':
					fputc(m_opStack.pop(), stdout);
					fflush(stdout);
					break;

				case '?':
					m_opStack.push(m_opStack.size());
					break;

				case 'Q':
					m_pc	= m_callStack.pop();
					break;

				case '[':
					m_callStack.push(m_pc);
					break;

				case ']':
					m_pc	= m_callStack.peek();
					break;

				case 'Z':
					arg1	= m_opStack.pop();
					if (arg1 > 0) {
						++m_pc;
					}
					break;

				case 'B':
					m_pc	= findNext(']', m_pc) + 1;
					m_callStack.drop();
					break;

				case ':':
					m_words[m_program[m_pc]]	= m_pc + 1;
					m_pc	= findNext(':', m_pc + 2) + 1;
					break;

				case '!':
					m_words[m_program[m_pc]]	= 0;
					++m_pc;
					break;

				case '"':
					while (m_program[m_pc] != '"') {
						m_opStack.push(m_program[m_pc++]);
					}
					++m_pc;
					break;

				case '#':
					m_opStack.push(m_memSize);
					break;

				default:
					return;
			}
		} else {
			m_callStack.push(m_pc);
			m_pc	= m_words[code];
		}
	}
}

int CEnema::findNext(__uint_8 what, int startPos) const
{
	bool	inString	= false;

	for (int i = startPos; i < sizeof(m_program); ++i) {
		if (!inString) {
			if (m_program[i] == what) {
				return i;
			}
		}
		if (m_program[i] == '"') {
			inString	= !inString;
		}
	}
	return -1;
}

void CEnema::readProgram(const char *fileName)
{
	int		commentLevel	= 0;
	FILE	*file			= fopen(fileName, "r");
	int		c;

	if (NULL != file) {
		while ((c = fgetc(file)) != EOF) {
			switch (c) {
				case '\r':
				case '\n':
					// skip
					break;

				case '{':
					++commentLevel;
					break;

				case '}':
					--commentLevel;
					break;

				case '`': {
						std::string	str;

						while ((c = fgetc(file)) != EOF && c != '`') {
							str	+= c;
						}

						readProgram(str.c_str());
					}
					break;

				default:
					if (commentLevel == 0) {
						m_program[m_programEnd++]	= (__uint_8)c;
					}
					break;
			}
		}
		fclose(file);
	}
}

void CEnema::pushArg(int arg)
{
	m_opStack.push(arg);
}

int CEnema::popArg()
{
	return m_opStack.pop();
}

int CEnema::peekArg() const
{
	return m_opStack.peek();
}

int CEnema::argCount() const
{
	return m_opStack.size();
}

