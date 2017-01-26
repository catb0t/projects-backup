/*
 * Enema.h	$Revision: 1.2 $	$Date: 2002/11/10 16:13:54 $	MB
 */

#ifndef __Enema_h__
#define __Enema_h__

#ifndef __Stack_h__
#include "Stack.h"
#endif

typedef unsigned char	__uint_8;

class CEnema
{
	public:
		CEnema(int memSize);
		~CEnema();

		void	readProgram(const char *fileName);
		void	reset();
		void	run();
		
		void	pushArg(int arg);
		int		popArg();
		int		peekArg() const;
		int		argCount() const;

	private:
		int		findNext(__uint_8 what, int startPos) const;
		
		int			m_memSize;
		int			*m_memory;

		int			m_programEnd;
		__uint_8	m_program[16384];
		int			m_words[256];

		int			m_pc;
		
		CStack<int, 4096>	m_opStack;
		CStack<int, 256>	m_callStack;
};

#endif

