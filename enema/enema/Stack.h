/*
 * Stack.h	$Revision: 1.1 $	$Date: 2002/11/10 15:10:44 $	MB
 */

#ifndef __Stack_h__
#define __Stack_h__

template<class T, int SIZE> class CStack
{
	public:
		CStack() : m_pos(-1)	{}

		void	push(T value) {
			m_data[++m_pos]	= value;
		}

		T		pop() {
			return m_data[m_pos--];
		}

		T		peek() const {
			return m_data[m_pos];
		}

		int		size() const {
			return (m_pos + 1);
		}
		
		void	drop() {
			--m_pos;
		}

		void	dup() {
			push(peek());
		}

		void	swap() {
			T	tmp				= m_data[m_pos];
			
			m_data[m_pos]		= m_data[m_pos - 1];
			m_data[m_pos - 1]	= tmp;
		}

		void	rot() {
			T	tmp				= m_data[m_pos];
			
			m_data[m_pos]		= m_data[m_pos - 2];
			m_data[m_pos - 2]	= tmp;
		}
		
	private:
		int	m_pos;
		T	m_data[SIZE];
};

#endif

