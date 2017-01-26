It's hard to review code that doesn't work per se, but I'll try my hand at a style review anyways.

# General stuff

    func Search(re *regexp.Regexp, logs []string) []string {

Nice method signature! But, `exported function Search should have comment or be unexported`. I trust there are docstrings in your code, right? That's valuable stuff, don't omit it here!

    var lwg sync.WaitGroup
    var lresults = make([]string, 0)
    NumCPU := runtime.NumCPU() * 2
    var divided = make([][]string, 0)

Personally, I find this kinda hard to read. You should do this instead:

    var (
      lwg sync.WaitGroup
      divided  = make([][]string, 0)
      lresults = make([]string, 0)
      NumCPU   = runtime.NumCPU() * 2
    )

That's the handiwork of my IDE. The Go language distrobution comes with a lot of code quality tools for readability and static analysis, and you should really use them *often*. (Every save, perhaps?)

  	// Splits the log lines into sub slices based
	// on the number of CPUs available.

Yay, comments! `/* multiline comments are more readable, though */`.

  	ChunkSize := len(logs) / NumCPU
  	if ChunkSize == 0 {
  		ChunkSize = 0
  	}

First of all, `ChunkSize` would ideally be declared in the `var ()` block up there, because it seems like there are no other uses for `NumCPU`. Go is fastest when you are smart and efficient with your memory, so don't leave variables lying around for no reason.

Second, I find this pointless. Yes, I, too, cry at Go's lack of ternary operator, but it's missing for a reason. That being said, I don't understand why you are setting a variable to what it is... ?

  	if ChunkSize > 200000 {
  		log.Warnf("There are %s lines of logs available. Searching may take awhile.", humanize.Comma(int64(len(logs))))
  	}

`2e5` is more readable and more easily changeable later. Moreover, I don't understand the coersion to `int64` here. Does `humanize` really only like `int64`? That seems lame.

  	for ii := range divided {
  		lwg.Add(2)
  		total := len(divided[ii])
  		mid := total / 2
  		array := divided[ii]
  		first := array[:mid]
  		second := array[mid:]
  		go func(s []string) {
  			for _, xx := range s {
  				if re.MatchString(xx) {
  					locker.Lock()
  					lresults = append(lresults, xx)
  					locker.Unlock()
  				}
  			}
  			lwg.Done()
  		}(first)
  		go func(s []string) {
  			for _, xx := range s {
  				if re.MatchString(xx) {
  					locker.Lock()
  					lresults = append(lresults, xx)
  					locker.Unlock()
  				}
  			}
  			lwg.Done()
  		}(second)
  	}

Whoa. Alright:

 1. Naming. I understand it's hard; I struggle with it too: *every* coder does. But please, for the love of Go, either use `i`, `index` or `int_theIndexOfTheFreakinFullyQualifiedStringObjectWeAreIteratingOn`. `ii` is hard to pronounce, not rememberable... I hate it.

 1. As far as I can tell, these variables `total`, `mid`, `first`, `second` have exactly one use: right here in this loop. Remember what I said about Go being faster when you keep the work for the GC down to a minimum. I get it improves readability, but at a point, that stuff should just be inlined to keep the cache happy.

 1. I see zero difference between these `go func`s, because they're identical. Ideally, you would assign it to a local var and call it on `first` and `second`.

 1. I can't *run* your code right now, which means I can't make it testable and I can't ask `go race` to take a look at it. What I can tell you, from a glance, is that you're accessing the same resources through two goroutines at once. The `locker`, assuming it does what it says on the tin, is a good thought, but you're still locking them at the same time and it's a recipe for disaster in the form of race conditions. See [here](http://stackoverflow.com/questions/23713215/golang-avoiding-race-conditions), [here](http://golang.org/blog/race-detector), [here](https://golang.org/doc/articles/race_detector.html), and the other results from the first page of google results on "avoid race condition golang".


return lresults

This could be a bare `return` if you put `(lresults []string)` in the signature, which would in my opinion improve readability both of the codee and the generated docs.