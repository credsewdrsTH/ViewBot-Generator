#import Python Modules
import webbrowser, time
#main function
def main():
    # name program
    print("* * * * YouTube ViewBot Generator * * * *")
    # Warning User
    print("Warning don't use you youtube acc to watch you vdo")
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