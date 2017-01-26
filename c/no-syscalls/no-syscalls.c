#define _GNU_SOURCE 1
#include <stddef.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/ptrace.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <sys/user.h>
#include <sys/wait.h>
#include <errno.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#if defined __linux__
# define SYS_unimplemented -1L
# if defined __i386__
#  define SYSCALL_NUMBER_REG regs.orig_eax
#  define SYSCALL_ARG1_REG   regs.ebx
#  define SYSCALL_ARG2_REG   regs.ecx
#  define SYSCALL_ARG3_REG   regs.edx
#  define SYSCALL_ARG4_REG   regs.esi
#  define SYSCALL_RESULT_REG regs.eax
# elif defined __x86_64__
#  define SYSCALL_NUMBER_REG regs.orig_rax
#  define SYSCALL_ARG1_REG   regs.rdi
#  define SYSCALL_ARG2_REG   regs.rsi
#  define SYSCALL_ARG3_REG   regs.rdx
#  define SYSCALL_ARG4_REG   regs.r10
#  define SYSCALL_RESULT_REG regs.rax
# else
#  error "Need to know system call convention for this CPU"
# endif
#else
# error "Need to know system call convention for this OS"
#endif

static long
xptrace(int request, pid_t pid, void *addr, void *data)
{
  errno == 0;
  long rv = ptrace(request, pid, addr, data);
  if (rv == -1 && errno) {
    perror("ptrace");
    if (pid != 0) kill(pid, SIGKILL);
    exit(1);
  }
  return rv;
}
#define GET_REG_(pid, x) \
  xptrace(PTRACE_PEEKUSER, pid, (void*)offsetof(struct user, x), 0)
#define GET_REG(pid, x) GET_REG_(pid, SYSCALL_##x##_REG)
#define SET_REG_(pid, x, v) \
  xptrace(PTRACE_POKEUSER, pid, (void*)offsetof(struct user, x), (void*)v)
#define SET_REG(pid, x, v) SET_REG_(pid, SYSCALL_##x##_REG, v)

/* This function defines the system-call policy.  */
static int
deny_syscall(pid_t pid, int scnum, int deny_all, int allow_stderr)
{
  switch (scnum) {
  /* These syscalls are unconditionally allowed (when not in -e mode);
     they perform input, or change only process-local state. */
#ifdef SYS_access
  case SYS_access:
#endif
#ifdef SYS_alarm
  case SYS_alarm:
#endif
#ifdef SYS_arch_prctl
  case SYS_arch_prctl:
#endif
#ifdef SYS_brk
  case SYS_brk:
#endif
#ifdef SYS_capget
  case SYS_capget:
#endif
#ifdef SYS_clock_getres
  case SYS_clock_getres:
#endif
#ifdef SYS_clock_gettime
  case SYS_clock_gettime:
#endif
#ifdef SYS_clock_nanosleep
  case SYS_clock_nanosleep:
#endif
#ifdef SYS_close
  case SYS_close:
#endif
#ifdef SYS_dup
  case SYS_dup:
#endif
#ifdef SYS_dup2
  case SYS_dup2:
#endif
#ifdef SYS_dup3
  case SYS_dup3:
#endif
#ifdef SYS_epoll_create
  case SYS_epoll_create:
#endif
#ifdef SYS_epoll_create1
  case SYS_epoll_create1:
#endif
#ifdef SYS_epoll_ctl
  case SYS_epoll_ctl:
#endif
#ifdef SYS_epoll_ctl_old
  case SYS_epoll_ctl_old:
#endif
#ifdef SYS_epoll_pwait
  case SYS_epoll_pwait:
#endif
#ifdef SYS_epoll_wait
  case SYS_epoll_wait:
#endif
#ifdef SYS_epoll_wait_old
  case SYS_epoll_wait_old:
#endif
#ifdef SYS_eventfd
  case SYS_eventfd:
#endif
#ifdef SYS_eventfd2
  case SYS_eventfd2:
#endif
#ifdef SYS_execve
  case SYS_execve:
#endif
#ifdef SYS_execveat
  case SYS_execveat:
#endif
#ifdef SYS_faccessat
  case SYS_faccessat:
#endif
#ifdef SYS_fadvise64
  case SYS_fadvise64:
#endif
#ifdef SYS_fadvise64_64
  case SYS_fadvise64_64:
#endif
#ifdef SYS_fanotify_init
  case SYS_fanotify_init:
#endif
#ifdef SYS_fanotify_mark
  case SYS_fanotify_mark:
#endif
#ifdef SYS_fgetxattr
  case SYS_fgetxattr:
#endif
#ifdef SYS_flistxattr
  case SYS_flistxattr:
#endif
#ifdef SYS_fstat
  case SYS_fstat:
#endif
#ifdef SYS_fstat64
  case SYS_fstat64:
#endif
#ifdef SYS_fstatat64
  case SYS_fstatat64:
#endif
#ifdef SYS_fstatfs
  case SYS_fstatfs:
#endif
#ifdef SYS_fstatfs64
  case SYS_fstatfs64:
#endif
#ifdef SYS_ftime
  case SYS_ftime:
#endif
#ifdef SYS_futex
  case SYS_futex:
#endif
#ifdef SYS_getcpu
  case SYS_getcpu:
#endif
#ifdef SYS_getcwd
  case SYS_getcwd:
#endif
#ifdef SYS_getdents
  case SYS_getdents:
#endif
#ifdef SYS_getdents64
  case SYS_getdents64:
#endif
#ifdef SYS_getegid
  case SYS_getegid:
#endif
#ifdef SYS_getegid32
  case SYS_getegid32:
#endif
#ifdef SYS_geteuid
  case SYS_geteuid:
#endif
#ifdef SYS_geteuid32
  case SYS_geteuid32:
#endif
#ifdef SYS_getgid
  case SYS_getgid:
#endif
#ifdef SYS_getgid32
  case SYS_getgid32:
#endif
#ifdef SYS_getgroups
  case SYS_getgroups:
#endif
#ifdef SYS_getgroups32
  case SYS_getgroups32:
#endif
#ifdef SYS_getitimer
  case SYS_getitimer:
#endif
#ifdef SYS_get_kernel_syms
  case SYS_get_kernel_syms:
#endif
#ifdef SYS_get_mempolicy
  case SYS_get_mempolicy:
#endif
#ifdef SYS_getpeername
  case SYS_getpeername:
#endif
#ifdef SYS_getpgid
  case SYS_getpgid:
#endif
#ifdef SYS_getpgrp
  case SYS_getpgrp:
#endif
#ifdef SYS_getpid
  case SYS_getpid:
#endif
#ifdef SYS_getpmsg
  case SYS_getpmsg:
#endif
#ifdef SYS_getppid
  case SYS_getppid:
#endif
#ifdef SYS_getpriority
  case SYS_getpriority:
#endif
#ifdef SYS_getrandom
  case SYS_getrandom:
#endif
#ifdef SYS_getresgid
  case SYS_getresgid:
#endif
#ifdef SYS_getresgid32
  case SYS_getresgid32:
#endif
#ifdef SYS_getresuid
  case SYS_getresuid:
#endif
#ifdef SYS_getresuid32
  case SYS_getresuid32:
#endif
#ifdef SYS_getrlimit
  case SYS_getrlimit:
#endif
#ifdef SYS_get_robust_list
  case SYS_get_robust_list:
#endif
#ifdef SYS_getrusage
  case SYS_getrusage:
#endif
#ifdef SYS_getsid
  case SYS_getsid:
#endif
#ifdef SYS_getsockname
  case SYS_getsockname:
#endif
#ifdef SYS_getsockopt
  case SYS_getsockopt:
#endif
#ifdef SYS_get_thread_area
  case SYS_get_thread_area:
#endif
#ifdef SYS_gettid
  case SYS_gettid:
#endif
#ifdef SYS_gettimeofday
  case SYS_gettimeofday:
#endif
#ifdef SYS_getuid
  case SYS_getuid:
#endif
#ifdef SYS_getuid32
  case SYS_getuid32:
#endif
#ifdef SYS_getxattr
  case SYS_getxattr:
#endif
#ifdef SYS_inotify_add_watch
  case SYS_inotify_add_watch:
#endif
#ifdef SYS_inotify_init
  case SYS_inotify_init:
#endif
#ifdef SYS_inotify_init1
  case SYS_inotify_init1:
#endif
#ifdef SYS_inotify_rm_watch
  case SYS_inotify_rm_watch:
#endif
#ifdef SYS_ioprio_get
  case SYS_ioprio_get:
#endif
#ifdef SYS_kcmp
  case SYS_kcmp:
#endif
#ifdef SYS_lgetxattr
  case SYS_lgetxattr:
#endif
#ifdef SYS_listxattr
  case SYS_listxattr:
#endif
#ifdef SYS_llistxattr
  case SYS_llistxattr:
#endif
#ifdef SYS_lookup_dcookie
  case SYS_lookup_dcookie:
#endif
#ifdef SYS_lseek
  case SYS_lseek:
#endif
#ifdef SYS_lstat
  case SYS_lstat:
#endif
#ifdef SYS_lstat64
  case SYS_lstat64:
#endif
#ifdef SYS_madvise
  case SYS_madvise:
#endif
#ifdef SYS_mbind
  case SYS_mbind:
#endif
#ifdef SYS_mincore
  case SYS_mincore:
#endif
#ifdef SYS_mlock
  case SYS_mlock:
#endif
#ifdef SYS_mlockall
  case SYS_mlockall:
#endif
#ifdef SYS_mprotect
  case SYS_mprotect:
#endif
#ifdef SYS_mremap
  case SYS_mremap:
#endif
#ifdef SYS_munlock
  case SYS_munlock:
#endif
#ifdef SYS_munlockall
  case SYS_munlockall:
#endif
#ifdef SYS_munmap
  case SYS_munmap:
#endif
#ifdef SYS_name_to_handle_at
  case SYS_name_to_handle_at:
#endif
#ifdef SYS_nanosleep
  case SYS_nanosleep:
#endif
#ifdef SYS_newfstatat
  case SYS_newfstatat:
#endif
#ifdef SYS_nice
  case SYS_nice:
#endif
#ifdef SYS_oldfstat
  case SYS_oldfstat:
#endif
#ifdef SYS_oldlstat
  case SYS_oldlstat:
#endif
#ifdef SYS_oldolduname
  case SYS_oldolduname:
#endif
#ifdef SYS_oldstat
  case SYS_oldstat:
#endif
#ifdef SYS_olduname
  case SYS_olduname:
#endif
#ifdef SYS_pause
  case SYS_pause:
#endif
#ifdef SYS_perf_event_open
  case SYS_perf_event_open:
#endif
#ifdef SYS_personality
  case SYS_personality:
#endif
#ifdef SYS_pivot_root
  case SYS_pivot_root:
#endif
#ifdef SYS_poll
  case SYS_poll:
#endif
#ifdef SYS_ppoll
  case SYS_ppoll:
#endif
#ifdef SYS_prctl
  case SYS_prctl:
#endif
#ifdef SYS_pread64
  case SYS_pread64:
#endif
#ifdef SYS_preadv
  case SYS_preadv:
#endif
#ifdef SYS_prlimit64
  case SYS_prlimit64:
#endif
#ifdef SYS_pselect6
  case SYS_pselect6:
#endif
#ifdef SYS_query_module
  case SYS_query_module:
#endif
#ifdef SYS_read
  case SYS_read:
#endif
#ifdef SYS_readahead
  case SYS_readahead:
#endif
#ifdef SYS_readdir
  case SYS_readdir:
#endif
#ifdef SYS_readlink
  case SYS_readlink:
#endif
#ifdef SYS_readlinkat
  case SYS_readlinkat:
#endif
#ifdef SYS_readv
  case SYS_readv:
#endif
#ifdef SYS_recvfrom
  case SYS_recvfrom:
#endif
#ifdef SYS_recvmmsg
  case SYS_recvmmsg:
#endif
#ifdef SYS_recvmsg
  case SYS_recvmsg:
#endif
#ifdef SYS_remap_file_pages
  case SYS_remap_file_pages:
#endif
#ifdef SYS_request_key
  case SYS_request_key:
#endif
#ifdef SYS_restart_syscall
  case SYS_restart_syscall:
#endif
#ifdef SYS_rt_sigaction
  case SYS_rt_sigaction:
#endif
#ifdef SYS_rt_sigpending
  case SYS_rt_sigpending:
#endif
#ifdef SYS_rt_sigprocmask
  case SYS_rt_sigprocmask:
#endif
#ifdef SYS_rt_sigreturn
  case SYS_rt_sigreturn:
#endif
#ifdef SYS_rt_sigsuspend
  case SYS_rt_sigsuspend:
#endif
#ifdef SYS_rt_sigtimedwait
  case SYS_rt_sigtimedwait:
#endif
#ifdef SYS_sched_getaffinity
  case SYS_sched_getaffinity:
#endif
#ifdef SYS_sched_getattr
  case SYS_sched_getattr:
#endif
#ifdef SYS_sched_getparam
  case SYS_sched_getparam:
#endif
#ifdef SYS_sched_get_priority_max
  case SYS_sched_get_priority_max:
#endif
#ifdef SYS_sched_get_priority_min
  case SYS_sched_get_priority_min:
#endif
#ifdef SYS_sched_getscheduler
  case SYS_sched_getscheduler:
#endif
#ifdef SYS_sched_rr_get_interval
  case SYS_sched_rr_get_interval:
#endif
#ifdef SYS_sched_setaffinity
  case SYS_sched_setaffinity:
#endif
#ifdef SYS_sched_setattr
  case SYS_sched_setattr:
#endif
#ifdef SYS_sched_setparam
  case SYS_sched_setparam:
#endif
#ifdef SYS_sched_setscheduler
  case SYS_sched_setscheduler:
#endif
#ifdef SYS_sched_yield
  case SYS_sched_yield:
#endif
#ifdef SYS_select
  case SYS_select:
#endif
#ifdef SYS_setfsgid
  case SYS_setfsgid:
#endif
#ifdef SYS_setfsgid32
  case SYS_setfsgid32:
#endif
#ifdef SYS_setfsuid
  case SYS_setfsuid:
#endif
#ifdef SYS_setfsuid32
  case SYS_setfsuid32:
#endif
#ifdef SYS_setgid
  case SYS_setgid:
#endif
#ifdef SYS_setgid32
  case SYS_setgid32:
#endif
#ifdef SYS_setgroups
  case SYS_setgroups:
#endif
#ifdef SYS_setgroups32
  case SYS_setgroups32:
#endif
#ifdef SYS_setitimer
  case SYS_setitimer:
#endif
#ifdef SYS_setns
  case SYS_setns:
#endif
#ifdef SYS_setpgid
  case SYS_setpgid:
#endif
#ifdef SYS_setpriority
  case SYS_setpriority:
#endif
#ifdef SYS_setregid
  case SYS_setregid:
#endif
#ifdef SYS_setregid32
  case SYS_setregid32:
#endif
#ifdef SYS_setresgid
  case SYS_setresgid:
#endif
#ifdef SYS_setresgid32
  case SYS_setresgid32:
#endif
#ifdef SYS_setresuid
  case SYS_setresuid:
#endif
#ifdef SYS_setresuid32
  case SYS_setresuid32:
#endif
#ifdef SYS_setreuid
  case SYS_setreuid:
#endif
#ifdef SYS_setreuid32
  case SYS_setreuid32:
#endif
#ifdef SYS_setrlimit
  case SYS_setrlimit:
#endif
#ifdef SYS_set_robust_list
  case SYS_set_robust_list:
#endif
#ifdef SYS_setsid
  case SYS_setsid:
#endif
#ifdef SYS_set_thread_area
  case SYS_set_thread_area:
#endif
#ifdef SYS_set_tid_address
  case SYS_set_tid_address:
#endif
#ifdef SYS_setuid
  case SYS_setuid:
#endif
#ifdef SYS_setuid32
  case SYS_setuid32:
#endif
#ifdef SYS_sigaction
  case SYS_sigaction:
#endif
#ifdef SYS_sigaltstack
  case SYS_sigaltstack:
#endif
#ifdef SYS_signal
  case SYS_signal:
#endif
#ifdef SYS_signalfd
  case SYS_signalfd:
#endif
#ifdef SYS_signalfd4
  case SYS_signalfd4:
#endif
#ifdef SYS_sigpending
  case SYS_sigpending:
#endif
#ifdef SYS_sigprocmask
  case SYS_sigprocmask:
#endif
#ifdef SYS_sigreturn
  case SYS_sigreturn:
#endif
#ifdef SYS_sigsuspend
  case SYS_sigsuspend:
#endif
#ifdef SYS_socketpair
  case SYS_socketpair:
#endif
#ifdef SYS_stat
  case SYS_stat:
#endif
#ifdef SYS_stat64
  case SYS_stat64:
#endif
#ifdef SYS_statfs
  case SYS_statfs:
#endif
#ifdef SYS_statfs64
  case SYS_statfs64:
#endif
#ifdef SYS_sysfs
  case SYS_sysfs:
#endif
#ifdef SYS_sysinfo
  case SYS_sysinfo:
#endif
#ifdef SYS_time
  case SYS_time:
#endif
#ifdef SYS_timer_create
  case SYS_timer_create:
#endif
#ifdef SYS_timer_delete
  case SYS_timer_delete:
#endif
#ifdef SYS_timerfd_create
  case SYS_timerfd_create:
#endif
#ifdef SYS_timerfd_gettime
  case SYS_timerfd_gettime:
#endif
#ifdef SYS_timerfd_settime
  case SYS_timerfd_settime:
#endif
#ifdef SYS_timer_getoverrun
  case SYS_timer_getoverrun:
#endif
#ifdef SYS_timer_gettime
  case SYS_timer_gettime:
#endif
#ifdef SYS_timer_settime
  case SYS_timer_settime:
#endif
#ifdef SYS_times
  case SYS_times:
#endif
#ifdef SYS_ugetrlimit
  case SYS_ugetrlimit:
#endif
#ifdef SYS_ulimit
  case SYS_ulimit:
#endif
#ifdef SYS_umask
  case SYS_umask:
#endif
#ifdef SYS_uname
  case SYS_uname:
#endif
#ifdef SYS_unshare
  case SYS_unshare:
#endif
#ifdef SYS_uselib
  case SYS_uselib:
#endif
#ifdef SYS_ustat
  case SYS_ustat:
#endif
#ifdef SYS_wait4
  case SYS_wait4:
#endif
#ifdef SYS_waitid
  case SYS_waitid:
#endif
#ifdef SYS_waitpid
  case SYS_waitpid:
#endif
    return deny_all;

#ifdef SYS_exit
  case SYS_exit:
#endif
#ifdef SYS_exit_group
  case SYS_exit_group:
#endif
    /* Special case: exiting is allowed, even in -e mode,
       but the exit status is forced to 0. */
    SET_REG(pid, ARG1, 0);
    return 0;

#ifdef SYS_fcntl
  case SYS_fcntl:
#endif
#ifdef SYS_fcntl64
  case SYS_fcntl64:
#endif
    /* Special case: fcntl is allowed, but only for the *FD and *FL
       operations.  This is a compromise between not allowing it at
       all, which would break some interpreters, and trying to go
       through the dozens of extended ops and figure out which ones
       can affect global state.  */
    {
      int cmd = GET_REG(pid, ARG2);
      if (cmd == F_DUPFD || cmd == F_DUPFD_CLOEXEC ||
          cmd == F_GETFD || cmd == F_SETFD || cmd == F_SETFL || cmd == F_GETFL)
        return deny_all;
    }
    return 1;

#ifdef SYS_kill
  case SYS_kill:
#endif
#ifdef SYS_rt_sigqueueinfo
  case SYS_rt_sigqueueinfo:
#endif
#ifdef SYS_rt_tgsigqueueinfo
  case SYS_rt_tgsigqueueinfo:
#endif
#ifdef SYS_tkill
  case SYS_tkill:
#endif
#ifdef SYS_tgkill
  case SYS_tgkill:
#endif
    /* Special case: kill is allowed if and only if directed to the calling
       process. */
    {
      pid_t kpid = GET_REG(pid, ARG1);
      if (kpid == pid)
        return deny_all;
    }
    return 1;

#ifdef SYS_mmap
  case SYS_mmap:
#endif
#ifdef SYS_mmap2
  case SYS_mmap2:
#endif
    /* Special case: mmap is allowed if it is private or read-only.  */
    {
      int prot  = GET_REG(pid, ARG3);
      int flags = GET_REG(pid, ARG4);
      if ((flags & (MAP_SHARED|MAP_PRIVATE)) == MAP_PRIVATE)
        return deny_all;
      if (!(prot & PROT_WRITE))
        return deny_all;
    }
    return 1;

    /* Special case: open() variants are allowed only if read-only and
       not creating. */
#ifdef SYS_open
  case SYS_open:
#endif
#ifdef SYS_openat
  case SYS_openat:
#endif
#ifdef SYS_open_by_handle_at
  case SYS_open_by_handle_at:
#endif
    {
      int flags = ((scnum == SYS_open)
                   ? GET_REG(pid, ARG2)
                   : GET_REG(pid, ARG3));
      if (!(flags & O_CREAT) && ((flags & O_ACCMODE) == O_RDONLY))
        return deny_all;
    }
    return 1;

#ifdef SYS_write
  case SYS_write:
#endif
#ifdef SYS_write64
  case SYS_write64:
#endif
#ifdef SYS_writev
  case SYS_writev:
#endif
#ifdef SYS_pwrite
  case SYS_pwrite:
#endif
#ifdef SYS_pwrite64
  case SYS_pwrite64:
#endif
#ifdef SYS_pwritev
  case SYS_pwritev:
#endif
    /* Special case: optionally, the program is allowed to write to
       stderr.  This opens a gaping hole in the policy, but it can be
       quite entertaining to watch programs moan about how nothing works. */
    if (allow_stderr) {
      int fd = GET_REG(pid, ARG1);
      if (fd == 2)
        return 0;
    }
    return 1;

  default:
    /* All other system calls are unconditionally denied. */
    return 1;
  }
}

static void
usage(char *progname)
{
  fprintf(stderr, "usage: %s [-adeS] program args...\n", progname);
  fputs("\t-a  log allowed system calls\n"
        "\t-d  log denied system calls\n"
        "\t-e  deny everything, not just output\n"
        "\t-S  permit writes to stderr\n", stderr);
  exit(2);
}

int
main(int argc, char **argv)
{
  pid_t pid;
  int   status;
  int   opt;
  long  last_syscall = SYS_unimplemented;
  int   last_allowed = 0;
  int   after_execve = 0;
  int   trace_active = 0;
  int   allow_stderr = 0;
  int   deny_all     = 0;
  int   log_allowed  = 0;
  int   log_denied   = 0;

  while ((opt = getopt(argc, argv, "+adeS")) != -1) {
    switch (opt) {
    case 'a': log_allowed  = 1; break;
    case 'd': log_denied   = 1; break;
    case 'e': deny_all     = 1; break;
    case 'S': allow_stderr = 1; break;
    default:
      usage(argv[0]);
    }
  }
  if (optind == argc) {
    usage(argv[0]);
  }

  setvbuf(stdout, 0, _IOLBF, 0);
  setvbuf(stderr, 0, _IOLBF, 0);

  pid = fork();
  if (pid == -1) {
    perror("fork");
    exit(1);

  } else if (pid == 0) {
    raise(SIGSTOP); /* synch with parent */
    execvp(argv[optind], argv+optind);
    perror("execvp");
    exit(1);
  }

  /* If we get here, we are the parent. */
  for (;;) {
    pid_t rv = waitpid(pid, &status, WUNTRACED);
    if (rv != pid) {
      perror("waitpid");
      kill(pid, SIGKILL);
      exit(1);
    }
    if (!WIFSTOPPED(status)) {
      if (WIFEXITED(status))
        printf("Program exited, status = %d\n", WEXITSTATUS(status));
      else if (WIFSIGNALED(status))
        printf("Program killed by signal %d\n", WTERMSIG(status));
      else {
        printf("Un-decodable status %04x\n", status);
        kill(pid, SIGKILL); /* just in case */
      }
      exit(0);
    }
    if (WSTOPSIG(status) == SIGSTOP && !trace_active) {
      /* This is the raise(SIGSTOP) on the child side of the fork. */
      trace_active = 1;
      xptrace(PTRACE_SEIZE, pid, 0, (void*)PTRACE_O_TRACESYSGOOD);
      xptrace(PTRACE_SYSCALL, pid, 0, 0);
    }
    else if (WSTOPSIG(status) == (SIGTRAP|0x80)) {
      if (last_syscall == SYS_unimplemented) {
        last_syscall = GET_REG(pid, NUMBER);
        /* The child process is allowed to execute normally until an
           execve() succeeds.  */
        if (after_execve && deny_syscall(pid, last_syscall,
                                         deny_all, allow_stderr)) {
          last_allowed = 0;
          SET_REG(pid, NUMBER, SYS_unimplemented);
        } else {
          last_allowed = 1;
          if (log_allowed) {
            /* Log this now, we may not get another chance. */
            printf("syscall %ld...\n", last_syscall);
          }
        }
      } else {
        if (last_allowed ? log_allowed : log_denied) {
          long scret = GET_REG(pid, RESULT);
          printf("syscall %ld%s = %ld\n",
                 last_syscall, last_allowed ? "" : " (denied)", scret);
        }
        if (last_allowed && (last_syscall == SYS_execve)) {
          long scret = GET_REG(pid, RESULT);
          if (scret == 0)
            after_execve = 1;
        }
        last_syscall = SYS_unimplemented;
      }
      xptrace(PTRACE_SYSCALL, pid, 0, 0);
    }
    else if (WSTOPSIG(status) == SIGTRAP) {
      /* Swallow all SIGTRAPs, they are probably spurious debug events. */
      xptrace(PTRACE_SYSCALL, pid, 0, 0);
    } else {
      /* Allow all normal signals to proceed unmolested. */
      if (log_allowed) {
        printf("process received signal %d\n", WSTOPSIG(status));
      }
      xptrace(PTRACE_SYSCALL, pid, 0, (void*)(uintptr_t)WSTOPSIG(status));
    }
  }
}
