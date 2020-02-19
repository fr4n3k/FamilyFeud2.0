import CategoryGetter
import CategoryFinder

playing = True
while playing:
    will = input('what you want to do?: ')
    if will == '1':
        print('Please wait...')
        cats = CategoryFinder.main()
        for title, url in cats.items():
            print(f"{title} : {url.replace('https://www.thetoptens.com/', '').rstrip('/')}")
    elif will == '2':
        CategoryGetter.main()
    else:
        playing = False
