import csv
import operator

# 달별, 요일별 프린트를 표시하기 위한 리스트
months = ['9월', '10월', '11월', '12월']
weeks = ['월요일', '화요일', '수요일', '목요일', '금요일']

# 메뉴 분석을 위한 공통 클래스
class Restaurant :

    # csv 파일 이름을 받아서 변수 초기화
    def __init__(self,csv):
        self.csv = csv
        self.name = csv[0:-4]


    # { 해당메뉴 : 빈도수 } 사전 만들기
    def make_dic(self,list) :
        temp_dic = {}
        for line in list :
            for menu in line :
                if menu == '': continue
                if menu in temp_dic:
                    temp_dic[menu] += 1
                else:
                     temp_dic[menu] = 1
        return temp_dic


    # 높은 빈도수로 sorting
    def make_sort(self,food_dic) :
        temp_list = sorted(food_dic.items(), key=operator.itemgetter(1), reverse =True)
        return temp_list


    # 메뉴 프린트
    def food_print(self,list) :
        for rank in list :
            print(rank)


    # 학기에 몇 번 나오는지
    def semester(self) :
        with open('C:\\Users\\써니\\Desktop\\food\\'+self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            food_all = [line for line in csv_reader]
            food_dic = self.make_dic(food_all)
            food_list= self.make_sort(food_dic)

            print(" < 2018-2학기 " + self.name + " 식단 리스트 > ")
            self.food_print(food_list)


    # 달에 몇 번 나오는지
    def month(self) :
        with open('C:\\Users\\써니\\Desktop\\food\\'+self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # 9, 10, 11, 12월 달별로 계산할 리스트 생성
            month = [[] for row in range(4)]
            i = 0

            # 한플은 하루에 5가지 메뉴가 나온다.
            # 9월 4주 (5*4) /10월 5주 (5*5) / 11월 4주 (5*4), 12월 3주 (5*3)
            for line in csv_reader :
                if i < 20 : month[0].append(line)
                elif 20 <= i < 45 : month[1].append(line)
                elif 45 <= i < 65 : month[2].append(line)
                elif 65 <= i < 80 : month[3].append(line)
                i+=1

            # 달별로 만들어진 리스트를 사전으로 만들고, 소팅하여, 프린트
            print(" < 2018-2학기 " + self.name + " 달별 리스트 > ")
            for i in range(4) :
                food_dic = self.make_dic(month[i])
                food_list = self.make_sort(food_dic)

                print("<<" + months[i] + ">>")
                self.food_print(food_list)
                print('\n')


    # 요일에 몇 번 나오는지
    def week(self) :
        with open('C:\\Users\\써니\\Desktop\\food\\'+self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # 요일별로 계산할 리스트 생성
            week = [[] for row in range(5)]

            # 한 줄에는 5개 메뉴가 요일별로 들어있다.
            # for문을 돌려 메뉴를 요일별 리스트에 넣어준다.
            for line in csv_reader :
                i = 0
                for menu in line :
                    temp = []
                    temp.append(menu)
                    week[i].append(temp)
                    i+=1

            # 요일별로 만들어진 리스트를 사전으로 만들고, 소팅하여, 프린트
            print(" < 2018-2학기 " + self.name + " 요일별 리스트 > ")
            for i in range(5) :
                food_dic = self.make_dic(week[i])
                food_list = self.make_sort(food_dic)

                print("<<" + weeks[i] + ">>")
                self.food_print(food_list)
                print("\n")

#한플 클래스
class Hanple(Restaurant) : pass

#생과대 클래스
class Life_science(Restaurant) :

    # 메인메뉴만 추출
    def make_main(self,list):
        food_main = []
        for line in list:
            for menu in line:
                temp = menu.split(',')
                food_main.append(temp[0])
        return food_main


    # { 해당메뉴 : 빈도수 } 사전 만들기
    def make_dic(self,list) :
        temp_dic = {}
        for menu in list:
            if menu == '': continue
            if menu in temp_dic:
                temp_dic[menu] += 1
            else:
                temp_dic[menu] = 1
        return temp_dic


    # 학기에 몇 번 나오는지
    def semester(self) :
        with open('C:\\Users\\써니\\Desktop\\food\\'+self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            food_all = [line for line in csv_reader]
            food_main = self.make_main(food_all)
            food_dic = self.make_dic(food_main)
            food_list = self.make_sort(food_dic)

            print(" < 2018-2학기 " + self.name + " 식단 리스트 > ")
            self.food_print(food_list)


    # 달에 몇 번 나오는지
    def month(self):
        with open('C:\\Users\\써니\\Desktop\\food\\' + self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # 메인메뉴만 추출
            food_all = [line for line in csv_reader]
            food_main = self.make_main(food_all)

            # 9, 10, 11, 12월 달별로 계산할 리스트 생성
            month = [[] for row in range(4)]
            i = 0

            # 생과대 하루에 4가지의 메뉴가 나온다. (메뉴수 * 요일수 * 주)
            # 9월 4주 (4*5*4) /10월 5주 (4*5*5) / 11월 4주 (4*5*4), 12월 3주 (4*5*3) 계산
            for line in food_main:
                if i < 80:
                    month[0].append(line)
                elif 80 <= i < 180:
                    month[1].append(line)
                elif 180 <= i < 260:
                    month[2].append(line)
                elif 260 <= i < 320:
                    month[3].append(line)
                i += 1


            # 달별로 만들어진 리스트를 사전으로 만들고, 소팅하여, 프린트
            print(" < 2018-2학기 " + self.name + " 달별 리스트 > ")
            for i in range(4):
                food_dic = self.make_dic(month[i])
                food_list = self.make_sort(food_dic)

                print("<<" + months[i] + ">>")
                self.food_print(food_list)
                print('\n')


    # 요일에 몇 번 나오는지
    def week(self) :
        with open('C:\\Users\\써니\\Desktop\\food\\'+self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # 메인메뉴만 추출
            food_all = [line for line in csv_reader]
            food_main = self.make_main(food_all)

            # 요일별로 계산할 리스트 생성
            week = [[] for row in range(5)]

            # 메인메뉴 리스트를 읽되, 한 리스트에 모든 메뉴가 들어있다!
            # 5번씩 나눠서 요일별 리스트에 넣어줘야한다.
            i = 0
            for menu in food_main :
                if i % 5==0 : week[0].append(menu)
                elif i % 5 ==1 : week[1].append(menu)
                elif i % 5 == 2: week[2].append(menu)
                elif i % 5 == 3: week[3].append(menu)
                elif i % 5 == 4: week[4].append(menu)
                i+=1

            # 요일별로 만들어진 리스트를 사전으로 만들고, 소팅하여, 프린트
            print(" < 2018-2학기 " + self.name + " 요일별 리스트 > ")
            for i in range(5) :
                food_dic = self.make_dic(week[i])
                food_list = self.make_sort(food_dic)

                print("<<" + weeks[i] + ">>")
                self.food_print(food_list)
                print("\n")

#신소재 클래스
class New_material(Life_science) :

    def month(self):
        with open('C:\\Users\\써니\\Desktop\\food\\' + self.csv, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # 메인메뉴만 추출
            food_all = [line for line in csv_reader]
            food_main = self.make_main(food_all)

            # 9, 10, 11, 12월 달별로 계산할 리스트 생성
            month = [[] for row in range(4)]
            i = 0
            
            # 신소재 하루에 3가지의 메뉴가 나온다. (메뉴수 * 요일수 * 주)
	        # 9월 4주 (3*5*4) /10월 5주 (3*5*5) / 11월 4주 (3*5*4), 12월 3주 (3*5*3) 계산
            for line in food_main:
                if i < 60:
                    month[0].append(line)
                elif 60 <= i < 135:
                    month[1].append(line)
                elif 135 <= i < 195:
                    month[2].append(line)
                elif 195 <= i < 240:
                    month[3].append(line)
                i += 1

            # 달별로 만들어진 리스트를 사전으로 만들고, 소팅하여, 프린트
            print(" < 2018-2학기 " + self.name + " 달별 리스트 > ")
            for i in range(4):
                food_dic = self.make_dic(month[i])
                food_list = self.make_sort(food_dic)

                print("<<" + months[i] + ">>")
                self.food_print(food_list)
                print('\n')

#메인
def main() :
    print("나는 이번 학기 아쿠아 돈까스를 2번 밖에 먹지 못했다...")
    print("한양대 학식의 최고 존엄 [아쿠아 돈까스]를 어떻게 해야 만날 수 있을까...?")

    # 각 csv 파일로 object 생성
    r1 = Hanple('한플.csv')
    r2 = Life_science('생과대.csv')
    r3 = New_material('신소재.csv')

    r1.semester()
    r1.month()
    r1.week()

    r2.semester()
    r2.month()
    r2.week()

    r3.semester()
    r3.month()
    r3.week()


if __name__ == "__main__" :
    main()




