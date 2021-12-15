#import Python Modules
import webbrowser, time
#Name Program
print("* * * * YouTube ViewBot Generator * * * *")
# Warn User
print("Warning : Don't use your acc to watch your vdo")
#main function
def main():
    #for error
    try:
        # url input
        url = input("Enter url: ")
        #for page
        duration = input("Enter duration: ")
        # for new webpage 
        for i in range(5):
            webbrowser.open_new(url)
            time.sleep(int(duration))
        # break program
        Break:True
    # for error
    except:
        print("somethings went wrong")
    #looping code back
    Repeat = input("Would you like to run again ").lower()
    if Repeat == "yes":
        main()
    else:
        print("Bye")
        exit()
main()
#end
