[TOC]



参考手册：[cppreference.com](https://zh.cppreference.com/w/首页)

[GCC, the GNU Compiler Collection - GNU Project](https://gcc.gnu.org/)



## 关于STL



STL 即标准模板库（Standard Template Library），是 C++ 标准库的一部分，里面包含了一些模板化的通用的数据结构和算法。由于其模板化的特点，它能够兼容自定义的数据类型，避免大量的造轮子工作。NOI 和 ICPC 赛事都支持 STL 库的使用，因此合理利用 STL 可以避免编写无用算法，并且充分利用编译器对模板库优化提高效率。

```cpp
//c++万能头
#include <bits/stdc++.h>
```





### 数据转义

```cpp
//整型转义   0b二进制     0x十六进制
int n = 0b101;//n = 5;
int inf = 0x3f'3f'3f'3f;//可以插入 ' 作为分隔符，方便阅读而不影响编译
```

```cpp
//字符串取消转义 c++11     语法为string s = R"(......)";   括号内为字符串
string s = R"(hello\nworld)";//直接输出 hello\nworld，而不会将\n转义为换行
```





### 字符串元素统计

```cpp
//c++风格字符串
string a = "ab c\0de";
cout << a.size() << endl;      //=4 统计到\0(或输入按回车)
cout << a.length() << endl;    //=4 统计到\0(或输入按回车)
```

```cpp
//c语言风格字符串
char s[999] = "ab c\0de";
cout << strlen(s);		//=4
```






### 连续输入



以回车停止

```cpp
int arr[1005];
do { cin >> arr[i];i++; } while (cin.get() != '\n'); //用do..while否则会吞输第一个输入
```



以EOF停止

```cpp
//c++
int n;
while (cin >>n) {cout << n << endl; } //以EOF结束
while (cin >>n&&n != -1) {cout << n << endl; } //以输入-1结束

//c语言
int n;
while(scanf("%d",&n) != EOF) { printf("%d",n);} //以EOF结束
```





### swap

交换两个元素

```cpp
//交换两个值
int a = 10,b = 20;
swap(a,b);//交换后a = 20, b = 10
```

```cpp
//交换两个容器
vector<int>a = {1,2,3},b = {4,5};
swap(a,b);//交换后a = {4,5}  b = {1,2,3}
```



#### iter_swap

`iter_swap(it1,it2) ` 用于交换两个迭代器指向的值。
诺使用`swap(it1,it2)`，只是交换了两个“指向节点的指针”（即迭代器），而不是交换原容器中的节点。

```cpp
list<int>q = {1,2};
map<int,list<int>::iterator>mp;
mp[1] = q.begin();
mp[2] = next(q.begin(),1);

auto it = q.begin();
auto it2 = next(it);

for(auto x:q){
    cout << x << ' ';
}cout << endl;

iter_swap(it,it2);//或者使用swap(*it,*it2),而非swap(it,it2)

for(auto x:q){
    cout << x << ' ';
}cout << endl;

cout << *mp[1] << ' ' << *mp[2] << endl;
```



------



## cstring



### 常用函数

| 常用函数                                                     |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **min**(a,b)/**max**(a,b)；                                  | 返回a,b最小/最大的数                                         |
| a.**push_back**(x);                                          | 在末尾添加一个元素x                                          |
| a.**pop_back**(x);                                           | 删除末尾元素x                                                |
| a.**insert**(pos,x);                                         | 在pos点插入元素x                                             |
| s.**erase**(pos,len);                                        | 删除下标pos开始，长度为len的子串                             |
| a.**clear**();                                               | 清空元素                                                     |
| a.**replace**(pos,len,"abc");                                | 元素替换                                                     |
| a.**find**("abc"[,pos][从下标pos位置开始查找,不填默认为0]);  | 返回第一次出现目标字符串的位置,没有则返回string::npos(通常定义为-1或无穷大) |
| a.**find_last_of**("abc"[,pos][从下标pos位置开始,不填默认为0]); | 返回最后一次出现目标字符串的位置,没有则返回string::npos(通常定义为-1或无穷大) |
| **getline**(cin,str,c);                                      | 输入字符串str,包括空格和回车，遇到c(不写默认为‘\n’)停止      |
| str1.**compare**(str2);                                      | 比较两个字符串的字典序                                       |
| **memset**(arr,'c',sizeof arr);                              | 初始化char[]型字符串为字符‘c’，或将数组元素按字节初始化为0/-1/0x3f |
| a+=b;                                                        | 字符串合并                                                   |
| a.**size**();   a.**length**();                              | 返回字符串元素个数                                           |
| a.**empty**();                                               | 返回字符串是否为空                                           |
| **count**(a.begin(), a.end(), c);                            | 计数字符c出现的次数                                          |
| a.**substr**(pos,len);                                       | 返回下标从pos开始长度为len的子串 (诺pos越界则会异常报错,诺pos+len越界则只会拷贝到字符串末尾) |
| a.c_str();                                                   | 返回这个string对应的字符数组的头指针                         |







### to_string

> 数字转字符串

```cpp
int n = 114514;
string a = to_string(n);
```

```cpp
//字符串转数字
string a = "114514";
int n = atoi(a.c_str());//从第一位开始，遇到非数字停止，诺第一位不是数字则为0
```



### memset

> #include <cstring>
>
> 按字节初始化

```cpp
//char[]型字符串
char arr[100];
memset(arr,'a',sizeof arr);//可以初始化为任意字符
for (int i = 0;i < 100;i++) cout << arr[i];
```

```cpp
//非字符型数组
int arr[100];//按字节初始化，int为4字节
memset(arr, -1, sizeof arr);//一般初始化为-1、0、0x3f或-0x3f
//-1 => (1111 1111 1111 1111) = -1
//0  = (0000 0000 0000 0000) = 0
//0x3f = (3f 3f 3f 3f) = 0x3f3f3f3f = 1061109567 > 1e9
for (int i = 0;i < 100;i++) cout << arr[i];
```



对一个浮点类型的数memset(a,-1,sizeof a)元素会初始化为 nan(not a number)，与任何比较大小的结果都为false





### getline

> 带空格/回车输入字符串
>
> 有时需要在每组**第一次**使用前加getchar();缓冲，防止读入上一个数据的回车。

```cpp
string str;
getline(cin,str,c);//读取到字符c则停止,诺参数c不写，则默认读取到回车停止,c可以为('字符') ,('\n') ,(' ') 等
cout << str;
```



### find

> rfind则为逆向查找，从字符串后面往前查找
>
> 当find函数未找到要查找的子字符串时，它将返回常量值string::npos	通常定义为-1；或一个很大的无符号整数类型的值

```cpp
//查找目标字符串的下标
#include<iostream>
#include<string>
using namespace std;
int main() {
	string arr = "komeijikoishi";
    
    string target = "oi";
	int index = arr.find(target);//返回第一次出现目标字符串的位置
    if(index == -1)) cout << "不存在子串" << endl;
	else cout << index << endl;
    
	int index2 = arr.find("i", 5);	//从下标为5的位置开始查找
	cout << index2 << endl;

    
	int index3 = arr.find_first_of("i");	//查找目标字符串第一次出现的位置
	cout << index3 << endl;
	int index4 = arr.find_last_of("i");		//查找目标字符串最后一次出现的位置
	cout << index4 << endl;

	return 0;
}
```

```cpp
//查找目标字符串出现的中次数
string s, c;
  while (cin >> s >> c) {
    int index = 0;//用来存储不断更新最新找到的位置
    int sum = 0;//累加出现的次数
    while ((index = s.find(c,index)) != string::npos) {
      cout << "sum: " << sum+1 << " index: " << index <<endl;
      index += c.length();//上一次s中与c完全匹配的字符应跳过，不再比较
      sum++;
    }
    cout << sum << endl;     // lllllll中ll出现了3次
  }
```

```cpp
//查找字符串中，某一个字符出现的次数
string a = "abcdefga";
cout << count(a.begin(), a.end(), 'a');
```



### compare

> 比较字典序
>
> 区分大小写，从头开始依次比较字符对应ASCII码大小

```cpp
string A = "12345";
string B = "12454";
cout << A.compare(B);
//A>B 返回1；	A<B 返回-1;	A==B 返回0；
```

```cpp
//str_cmp比较char类型字符串的字典序
char A[] = "abc";
char B[] = "abc";
strcmp(A,B)
//A>B 返回1；	A<B 返回-1;	A==B 返回0；
```





### replace

> 字符替换

```cpp
//a.replace(pos,len,"str");  从pos位置开始，长度为len，替换为str
string a = "abcdefg";
a.replace(0, 4, "66");//或者用迭代器a.replace(a.begin(), a.begin() + 4, "66");
//replace(a.begin(),a.end(),'a','*');
cout << a;//66efg

//a.replace(pos,len,n,'c');	从pos位置开始，长度为len,替换为重复n次的字符c
string a = "abcdefg";
a.replace(0,4,3,'6');
```



```cpp
//将字符串中的a用b替换
replace(str.begin(), str.end(), 'a', 'b');  //需包含#include <algorithm> 
```





------



## cmath

### [常用函数](https://zh.cppreference.com/w/cpp/header/cmath)

| 常用函数                        |                                                 |
| ------------------------------- | ----------------------------------------------- |
| pow(a,b)                        | a^b次方                                         |
| sqrt(n)                         | sqrt开平方根  cbrt开立方                        |
| abs(n)                          | 绝对值                                          |
| ceil(n)，floor(n)，round(n)     | 向上取整， 向下取整 ，四舍五入取整              |
| round(n)                        | 四舍五入到整数                                  |
| log2(n)，log10(n)，log(n)       | 求以2/10/e为底的对数,logf、logl为单精度、高精度 |
| sin，cos，tan，asin，acos，atan | 三角函数                                        |





### 指数

#### pow

> n * pow(a,b);    //相当于$n*(a^b)$

```cpp
//pow参数类型和返回值类型均为浮点型，可能会导致输出与预期不符而wrong answer
int a = 1234;
cout << a*a << endl;//1522756
cout << pow(a, 2)<< endl;//1.52276e+06        可以用int n = pow(a,2)类型转换再输出n
```









#### exp



> exp(x);   返回 $e^x$，在 `double` 内，x 的有效区间为 [−708.4,709.8]







### 对数

#### log

```cpp
log(x);
```

| 函数     |                    |
| -------- | ------------------ |
| log(x)   | $lnx$，以 $e$ 为底 |
| log10(x) | $lgx$，以10为底    |
| log2(x)  | $log_2x$，以2为底  |



### 开根

#### sqrt

```cpp
sqrt(n);	//开平方根,参数为double
sqrtf(n);	//参数为float
sqrtl(n);	//高精度，参数类型是long double;防止long long类型强转为double的误差


pow(n,1.0/m);//开n次方（1.0/m或1/m.0）
```



#### cbrt

```cpp
cbrt(n);	//开三次方
```







### 绝对值

请使用C++的`std::abs`，而非C的`abs`，后者只针对`int`类型，容易造成计算错误

#### abs

```cpp
abs(n);
fabs(n);
fabsl(n);
```









### 取整

#### ceil

```cpp
double n = 1.5;
//向上取整	ceil(1.5) = 2;
ceil(n) = 2;
ceil(2/3) = 0;//相当于ceil(0)  
ceil(1.0*2/3) = 1;//整型相除应先转换为浮点型，再取整

```

#### floor

```cpp
double n = 1.5;
//向下取整	floor(1.5) = 1;
floor(n) = 1;	
```



#### round

```cpp
double n = 1.5;
//四舍五入取整
round(n);	//取最接近整数(中间情况下远离0取整)
pintf("%.2lf",n);//四舍五入保留2位小数,long double类型改为%.2Lf
round(n*100)/100;	 //四舍五入保留2位小数
```







### 三角函数

```cpp
sin(x);
cos(x);
tan(x);
    
asin(x);
acos(x);//acos(-1) = π
atan(x);//取值范围(-π/2,π/2)
```

```cpp
atan2(y,x);//返回原点至(y,x)的方位角(即与x轴的夹角),取值范围为(-π,π]。
//诺要以度数表示,将结果*180/π即可
//比atan稳定。当y远大于x时,atan计算结果是不稳定的;
```





------



## algorithm

### 常用函数

| 常用函数                        |                                                              |
| ------------------------------- | ------------------------------------------------------------ |
| sort(begin,end,cmp)             | cmp为空则默认升序排序                                        |
| is_sorted(begin,end)            | 返回所给序列是否已按排列(默认判断是否非递减)                 |
| lower_bound(begin,end,value)    | 返回第一个>=v值的迭代器(-begin()即为下标)                    |
| upper_bound(begin,end,value)    | 返回一个>v值的迭代器(-begin()即为下标)                       |
| count(begin,end,value)          | 计数v值出现了多少次                                          |
| count_if(begin,end,cmp)         | 按自定义cmp规则计数                                          |
| reverse(begin,end)              | 翻转所在区间数值                                             |
| find(begin,end,value)           | 返回v值第一次出现的迭代器,没有则返回指向容器末尾的迭代器     |
| erase(begin,end)                | 删除范围内元素                                               |
| unique(begin,end)               | [移除范围内的连续重复元素 ,返回去重之后的尾地址(使用前先排序)][实际并没有删除,只是将重复元素放到容器末尾,不改变容器大小] |
| next_permutation(begin,end)     | 将元素排列为下一个字典序,没有下一个则返回0，prev_permutation上一个字典序 |
| nth_element(begin,nth,end)      | 重排first~last中元素使第nth小的数在第nth位置,左边的数都小于它,右边的数都大于它 |
| max_element(begin,end)          | 返回所给范围内最大值的迭代器  min_element类似                |
| minmax({n1,n2,n3,...})          | 返回参数中的最小值和最大值，返回类型为pair<min,max>          |
| fill(begin,end,value)           | 将范围内元素赋值为value                                      |
| search(begin1,end1,begin2,end2) | 返回begin1~end1中第一次出现begin2 ~end2中的迭代器,没有则返回指向end1的迭代器 |



### sort

#### sort

> 语法：sort(begin, end, cmp);
>
> 其中begin为指向待sort()的数组的`第一个元素的指针`，end为指向待sort()的数组的`最后一个元素的下一个位置的指针`，cmp参数为排序准则(不写的话，默认从小到大进行排序);
>
> 时间复杂度：n*log2(n)

```c++
//从小到大
sort(arr, arr+10);   
sort(str.begin(),str.end());
//从大到小则cmp = greater<int>()
sort(arr, arr+10, greater<int>());   
sort(str.begin(),str.end(),greater<int>());
//或者sort(str.rbegin(),str.rend());//sort(a.rbegin(),a.rend()-1)//下标从1开始
```



自定义cmp排序准则

需注意：`sort`比较两个结构体，不能出现`a < b`和`b < a` 同时为真的情况，否则会运行错误

```cpp
//结构体排序
#include <iostream>
#include <algorithm>
using namespace std;
struct hero{ string name;int sco; };
void info(hero arr[], int len){
	string nameSeed[5] = {"小毛","小刘","小李","小张","小王"};
	for (int i = 0;i < len; i++) {
		arr[i].name += nameSeed[i];
		cout << "姓名：" << arr[i].name;
		cout << "\t请输入分数：";cin >> arr[i].sco;
	}
}

bool agerank(hero a, hero b) { 
    return a.sco > b.sco; 
    //自定义排序，以结构体sco大小为依据
}

void printInfo(hero arr[],int len) {
	cout << "\n\n\n排序后\n" << endl;
	for (int i = 0;i < len;i++) {
		cout << "姓名：" << arr[i].name << "\t分数：" << arr[i].sco << endl;
	}
}
int main() {
	hero arr[5];
	int len = sizeof(arr) / sizeof(arr[0]);
	info(arr, len);//1.输入信息
	sort(arr, arr+len,agerank);//2.排序
	printInfo(arr, len);//3.输出
}
```





#### stabl_sort

稳定排序，但需要额外的空间开销



#### partial_sort

将区间最小的前k个按升序排在前面

时间复杂度O(N*logM)    其中N为区间长度,M为前M个长度 

partial_sort(first, first+k, last);   
partial_sort(first, first+k, last, cmp);    //cmp不写默认升序 

```cpp
vector<int>a = {6,9,2,3,1,5,7,5,4};
partial_sort(a.begin(),a.begin()+5,a.end());
//a = 1 2 3 4 5 9 7 6 5 
```





#### partial_sort_copy

不改变原来的容器，而是先将选定的部分元素拷贝到另外指定的容器中，然后再对这部分元素进行排序。

partial_sort_copy(first1, last1, first2, last2);
partial_sort_copy(first1, last1, first2, last2, cmp);

```cpp
vector<int>a = {6,9,2,3,1,5,7,5,4},b(5);//诺b的大小不足5个,则会舍去后面的
partial_sort_copy(a.begin(),a.end(),b.begin(),b.begin()+5);//b = 1 2 3 4 5
```







#### is_sorted

返回值为bool类型

is_sorted(first,end);

> 判断区间元素是否已经排序,默认判断升序

is_sorted(first,end,cmp)

> ```cpp
> is_sorted(a.begin(),a.end(),[](auto &e1,auto &e2){return e1 > e2;}//是否非递增
> is_sorted(a.begin(),a.end(),[](auto &e1,auto &e2){return e1 >= e2;}//是否严格递减 
> ```







### reverse

reverse(begin,end) 翻转范围内的数

```cpp
reverse(str.begin(), str.end());	//字符串倒序
```

```cpp
reverse(a,a+n);    //数组的翻转，n为数组元素个数
```





### unique

  [移除范围内的连续重复元素 ,返回去重之后的尾部迭代器(使用前先排序)][实际并没有删除,只是将重复元素放到容器末尾,不改变容器大小]

```cpp
unique(v.begin()+1, v.end());
unique(a+1,a+n+1);
//int m = unique(a+1,a+n+1) - a - 1;
//unique前：2 3 3 4 4 5 8 9 9 
//unique后：2 3 4 5 8 9 8 9 9
//a[1~m] = {2 3 4 5 8 9}
```

```cpp
//配合erase删除 适用于容器如 vector
erase(unique(v.begin(),v.end()),v.end());
```



### count

在序列中统计某个值出现的次数

> cout<<count(arr.begin() , arr.end() , searchValue) << endl;

```cpp
#include <iostream>
using namespace std;
int main() {
	int n,x，arr[100]; cin >> n>>x;
	for (int i = 0;i < n;i++)
		cin >> arr[i];
	cout << count(arr,arr+n,x);
}
```



#### count_if

返回满足条件范围内的元素个数

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <int> myvector;
bool isEven(int elem){ return elem % 2 == 0;}
bool cmp(int elem) { return elem > 2; }
void main(){
	for (int i = 0;i < 9;i++){
		myvector.push_back(i+1);
		cout << myvector[i];
	}
	// 计算偶数个数
	int ctif = count_if(myvector.begin(), myvector.end(), isEven);
	// 计算大于2的个数
	int ctg = count_if(myvector.begin(), myvector.end(), cmp);
	cout << "偶数元素个数:" << ctif << endl;
	cout << "超过2的元素个数: " << ctg << endl;
}
```



### lower_bound

> 使用时需要保证数组为有序非递减

lower_bound( begin,end,num)：从数组的begin位置到end-1位置二分查找第一个**大于或等于num的数字**，找到返回该数字的地址，不存在则返回end。通过返回的地址减去起始地址begin,得到找到数字在数组中的下标。

upper_bound( begin,end,num)：从数组的begin位置到end-1位置二分查找第一个**大于num的数字**，找到返回该数字的地址，不存在则返回end。通过返回的地址减去起始地址begin,得到找到数字在数组中的下标。

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

vector<int>v;

int main() {
	for (int i = 1; i <= 9;i++) {
		v.push_back(i * 2);
		v.push_back(i * 2);
		v.push_back(i * 2);		
	}
	for(auto& i:v){
		cout << i << ' ';
	}puts("");

	int x; cin >> x;
    
	int it1 = lower_bound(begin(v), end(v), x) - begin(v);//尽量不要用auto
	int it2 = upper_bound(begin(v), end(v), x) - begin(v);
	if (it1 == size(v)) cout << -1 << "   ";
	else cout << it1 << "   ";

	if (it2 == size(v))  cout << -1 << endl;
	else cout << it << endl;
	
	return 0;
}
```

```cpp
// 例题:https://www.luogu.com.cn/problem/P2249
#include<iostream>
using namespace std;
int a[1000005];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for(int i = 1; i<=n; i++) {
        scanf("%d", &a[i]);
    }
    while(m--) {
        int x;
        scanf("%d", &x);

        int tot = lower_bound(a+1, a+n+1, x) - a;//返回第一个大于等于x的位置
        int ans = upper_bound(a+1, a+n+1, x) - a;//返回第一个大于x的位置 
        printf("%d\n", tot); 
    }
    
    return 0;
}
```



### next_permutation

prev_permutation求当前排列的上一个排列

求当前排列的下一个排列，当当前序列不存在下一个排列时，函数返回false，否则返回true。

```cpp
//全排列需要先对数组按升序排序
int arr[100];
int n; cin >> n;
for (int i = 0;i < n;i++)
    cin >> arr[i];

sort(arr, arr + n);

do {for (int i = 0; i < n; i++){
    cout << arr[i] << ' ';
    }cout << endl;
}
while (next_permutation(arr, arr + n));
```

```cpp
//prev_permutation求当前排列的上一个排列
string a = "cadb";
sort(a.begin(), a.end(),greater<int>());
do {cout << a << endl;
} while (prev_permutation(a.begin(), a.end()));
```



### nth_element

时间复杂度O(N)

nth_element(first,nth,last)会将重排first~last中元素使得小于 `*nth`的在其左边，大于等于 `*nth`的在其右边

```cpp
//求第k小数
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 5000006;
int a[N];

int main(){
	int n,m;cin >> n >> m;
	for(int i = 0;i < n;i++) scanf("%d",&a[i]);

	nth_element(a,a+m,a+n);

	cout << a[m];
}
```



### minmax_element

` minmax_element(first,last)`  

> 返回区间最小值和最大值的迭代器，返回类型为pair<min,max>
>
> ```cpp
> auto ans = minmax_element(a.begin(),a.end());
> cout << *ans.first << ' ' << *ans.second << endl;
> ```
>
> ```cpp
> auto [mn,mx] = minmax_element(a.begin(),a.end());
> cout << *mn << ' ' << *mx << endl;
> ```





`max_element(first,last)`     `min_element(first,last)`



> 返回区间`最大值`或 `最小值` 的迭代器
>
> ```cpp
> int mx = *max_element(a.begin(),a.end());
> int mn = *min_element(a.begin(),a.end());
> cout << mx << endl << mn << endl;
> ```





### minmax

元素个数大于两个要打花括号

**minmax({n1,n2,n3, ... })**  

> 返回最小的和最大的元素，返回类型为pair(min,max)
>
> ```cpp
> auto [mn,mx] = minmax({n1,n2,n3,n4});   //pair<int,int> ans = min({n1,n2,n3,n4});
> cout << mn << ' ' << mx << endl;
> ```



**min({n1,n2,n3, ... })**  

> 返回最小的元素  ，max类似
>
> ```cpp
> int mn = min({a1,a2,a3,a4});
> int mx = max({a1,a2,a3,a4});
> cout << mn << ' ' << mx << endl;
> ```





### 仅GNU

仅在GNU编译器可用，否则会编译错误

 ```
__lg(x)
 ```
  - 返回 $⌊log⁡_2x⌋$。
  - 时间复杂度 O(1)。
  - 常用于实现倍增、二进制运算等。





 ```
  __gcd(x,y)
 ```
  - 返回 gcd⁡(x,y)。
  - 复杂度是对数级别的，常数较小。
  - 注意，返回值的符号 **不一定** 是正。
  - 在 C++17 之前都是很常用的。





 ```cpp
 __builtin_popcount(x)	//返回 x 在二进制下 1 的个数
 __builtin_parity(x)		//返回 x 在二进制下 1 的个数的奇偶性，略快于 __builtin_popcount(x)&1
 __builtin_ffs(x)		//返回二进制下最后一个 1 是从右往左第几位(从低位到高位)
 __builtin_ctz(x)		//返回二进制下后导零的个数，x=0 时未定义
 __builtin_clz(x)		//返回二进制下前导零的个数，x=0 时未定义
 ```

  **复杂度约为 O(log⁡log⁡n) 且常数很小，一般比手写位运算快。**

如果 x 的类型是 long long，请务必使用 `__builtin_xxxll(x)`







------



## map


### 常用函数

| 常用函数         |                                                              |
| ---------------- | ------------------------------------------------------------ |
| m.begin()        | 返回指向map头部的迭代器                                      |
| m.end()          | 返回指向map末尾的迭代器                                      |
| m.insert({x,y})  | 插入元素(pair类型)                                           |
| m.clear()        | 删除所有元素                                                 |
| m.size()         | 返回map中元素的个数                                          |
| swap(m1,m2)      | 交换两个map容器的所有元素                                    |
| m.empty()        | 返回容器是否为空                                             |
| m.erase()        | 参数为一个迭代器或键值则删除该元素，参数为两个迭代器时则删除两个迭代器之间的元素O(logN) |
| m.find(x)        | 返回键值为x的元素的迭代器,不存在则返回end()                  |
| mp.lower_bound() | 返回一个迭代器，指向键值 >= x 的第一个元素                   |
| mp.upper_bound() | 返回一个迭代器，指向键值 > x 的第一个元素                    |



### 定义

map内部是自动排序的

> map<type1name,type2name> m1;//第一个是关键字key(每个关键字只能出现一次)的类型，第二个是对应的值value的类型
>
> 数据类型可以是string，char，int，iterator，pair等多种类型
>
> multimap<type1name,type2name> m2;可以有多个相同的键值对




### 插入元素

map<int, string> student;

```cpp
//1.用insert函数插入pair数据
student.insert(pair<int, string>(000, "student_zero"));
```

```cpp
//2.用insert函数插入value_type数据
student.insert(map<int, string>::value_type(001, "student_one"));
```

```cpp
//3.用"array"方式插入
mapStudent[1] = "student_first";
mapStudent[2] = "student_second";
```



### 访问元素

诺不确定一个元素是否存在，避免使用`[ ]`查找，而是要用 `find()` 函数。因为用 `[]` 如果不存在会新建一个元素反复使用会造成 TLE。

```cpp
//通过键值
#include <iostream>
#include <map>
using namespace std;
map<string,int>student;
int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++){
		string name; int num; 
		cin >> name >> num;
		student[name] = num;
	}
    //输入姓名 查找学号
	string find_name; cin >> find_name;
	cout << student[find_name] << endl;
	return 0;
}
```

```cpp
//for(auto &i: m) 遍历元素   c++11
#include <iostream>
#include <map>
using namespace std;
map<string, int>m;
int main() {
	for (int i = 0; i < 3;i++) {
		string s; cin >> s;
		int n; cin >> n;
		m[s] = n;
	}
	for (auto& i:m){
		cout << i.first << ' ' << i.second << endl;
	}
    for(pair<const string,int>& i:m){//键值不可修改
        cout << i.first << ' ' << i.second << endl;
    }
    for(auto& [x,y]:m){//c++17结构化绑定  //auto &[x,y] = *mp.begin();
        cout << x < " " << y << endl;
    }

	return 0;
}
```



```cpp
//通过迭代器遍历元素 	map<string, int>::iterator it = student.begin();
#include <iostream>
#include <map>
using namespace std;
map<string,int>student;
int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++){
		string name; int num; 
		cin >> name >> num;
		student[name] = num;
	}
    //遍历姓名及学号
	for (map<string, int>::iterator it = student.begin(); it != student.end(); it++)
		cout << it->first << " " << it->second << endl;
    
    //或
    for (map<string, int>::iterator it = student.begin(); it != student.end(); it++)
		cout << (*it).first << " " << (*it).second << endl;
}
```





### unordered_map

> #include <unordered_map> 
>
> unordered_map 容器等价为无序的 map 容器。
>
> 无法使用pair类型作为key

unordered_map通过相关的映射函数来加快寻找速度，因此，如果数据随机，unordered_map的插入和查询速度接近O(1)。但是由于hash冲突的存在，能被一些特意构造的数据卡到O(n)的时间复杂度，当然，我们可以通过手写hash函数的形式来尽量规避此类问题。





#### 重载

防止某些处心积虑的人卡 unordered_map。
使用pair、结构体等类型作为umap/uset的key值时，需要手动重载哈希函数，因为它们没有默认的哈希函数。

源自CFblog更强的哈希函数（ https://codeforces.com/blog/entry/62393）：

```cpp
const auto RAND = std::chrono::steady_clock::now().time_since_epoch().count();//#include <chrono>
struct hh {
    static int splitmix64(int x) {
		x += 0x9e3779b97f4a7c15;
		x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
		x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
		return x ^ (x >> 31);
	}
	int operator () (const int &x) const {
		return splitmix64(x + RAND);
	}
};

unordered_map<int,int,hh>mp;
//gp_hash_table<int,int,hh>hs;  //或者pd_ds的hash_table
```





------





## vector

> 向量（Vector）是一个封装了动态大小数组的顺序容器（Sequence Container）。跟任意其它类型容器一样，它能够存放各种类型的对象。可以简单的认为，向量是一个能够存放任意类型的动态数组。

> 使用STL向函数传递容器时使用&引用传递或者*指针传递，否则会发生拷贝构造，与数组不同
>
> ```cpp
> void function1(vector<int> vec)//传值		//值传递，会发拷贝构造，与数组不同
> void function2(vector<int>& vec)//传引用	//引用传递，不会发生拷贝构造
> void function3(vector<int>* vec)//传指针	//指针传递，不会发生拷贝构造
> ```
>

### 常用函数

| 常用函数                     |                                 |
| ---------------------------- | ------------------------------- |
| v.front/back()               | 返回第一/最后个元素             |
| v.push_back()/emplace_back() | 向容器末添加一个元素   O(1)     |
| v.pop_back()                 | 删除容器末的元素   O(1)         |
| v.insert()                   | 向容器中插入元素   O(n)         |
| v.erase(first,last)          | 删除指定位置元素  O(n)          |
| v.size()                     | 返回容器内元素个数              |
| v.empty()                    | 返回容器是否为空                |
| v.clear()                    | 清空容器                        |
| v1.compare(v2)               | 按字典序比较容器v1和v2          |
| v1.swap(v2)                  | 交换两个容器,vector特化版的swap |



```cpp
//支持两个容器比较   按字典序比较
vector<int>a{1,3,3,4};
vector<int>b{1,2,16,5,5};
cout << (a > b) << endl;
```



### 定义及初始化

```cpp
//不建议使用vector<bool>效率很低
//定义一个空的容器
vector<int>v1;
//定义一个空的vector类型数组
vector<int>arr[100];
//定义一个含有10个元素的容器
vector<int>v2(10);	//int类型默认初始化为0
//定义一个含有10个元素的容器，并将其初始化
vector<string>v3(10,"abc");
//定义二维数组v[n+1][26]每个元素初始化为INF
vector<vector<int>>dp(n+1,vector<int>(26,INF));
```



### 增删特定位置元素

> 时间复杂度O(1)~O(N)，常数较小

```cpp
A.push_back(x) ;//在末尾添加元素x	O(1)
A.pop_back();//删除末尾元素		O(1)
A.insert(pos,x);//在迭代器pos位置添加元素x	O(n)
A.erase(first,last);//删除迭代器first到last之间的元素	O(n)
A.clear();	//清空所有元素 O(n)
```

//通过迭代器：

```cpp
//insert(po,x) 在迭代器po位置插入元素x
vector<int> A = { 100,200,300,400,500,600 };
vector<int>::iterator it;	//通过迭代器访问容器
	
	it = A.begin();
	A.insert(it, 111); //向索引为0的位置插入元素111
	//输出内容为：111 100 200 300 400 500 600
	for (int i = 0; i < A.size(); i++) {
		cout << A[i] << " ";
	}
	cout << endl;

	it = A.begin() + 2;
	A.insert(it, 222); //向索引为2的位置插入元素222
	//输出内容为：111 100 222 200 300 400 500 600
	for (int i = 0; i < A.size(); i++) {
		cout << A[i] << " ";
	}
	cout << endl;

	it = A.end();
	A.insert(it, 999); //向A的末尾插入元素999
	//输出内容为：111 100 222 200 300 400 500 600 999
	for (int i = 0; i < A.size(); i++) {
		cout << A[i] << " ";
	}
	cout << endl;
```

```cpp
//erase() 函数来删除指定位置的元素
vector<int> A = { 100,200,300,400,500,600 };
vector<int>::iterator it;

	it = A.begin(); //索引为0的位置
	A.erase(it); //删除索引为0的位置的元素
	//输出内容为：200 300 400 500 600
	for (int i = 0; i < A.size(); i++) {
		cout << A[i] << " ";
	}
	cout << endl;

	it = A.begin() + 2; //索引为2的位置
	A.erase(it); //删除索引为2的位置的元素
	//输出内容为：200 300 500 600
	for (int i = 0; i < A.size(); i++) {
		cout << A[i] << " ";
	}
	cout << endl;
```



### 删除指定数值元素



```cpp
//如果能在目标vector中找到该数值的元素，直接删除
//如果目标vector中找不到该数值的元素，不做任何操作，不会报错
vector<int> A = { 100,200,300,400,500,600 };
A.erase(remove(A.begin(), A.end(), 500), A.end()); //删除数值为500的元素
A.erase(remove(A.begin(), A.end(), 700), A.end()); //删除数值为700的元素
//输出内容为：100 200 300 400 600
for (int i = 0; i < A.size(); i++) {
    cout << A[i] << " ";
}
cout << endl;
```

```cpp
//排序再去重 
sort(alls.begin(), alls.end());
alls.erase(unique(alls.begin(), alls.end()), alls.end());
	//unique把所有重复元素放到容器后面，再把不重复元素提前，返回最后一个不重复元素位置（algorithm）
	//erase删除最后一个不重复元素位置到数组末尾的位置的所有元素（vector）
```



### 查找指定数值的元素

```cpp
//使用 find() 函数查找    函数的返回值为迭代器或指针
vector<int> myVector = { 100,200,300,400,500,600 };
vector<int>::iterator it = find(myVector.begin(), myVector.end(), 500);
//输出内容为：目标元素的索引为: 4
if (it != myVector.end()) {
    cout << "目标元素的索引为: " << distance(myVector.begin(), it) <<endl;
}
else {
    cout << "没有找到" <<endl;
}
```

### 遍历元素

vector<int> v = { 100,200,300,400,500,600 };

```cpp
//通过迭代器
for (vector<int>::iterator i2 = v.begin(); i2 != v.end();i2++) {
	cout << *i2 << endl;//*i2解引用
}

//或者这里直接使用auto，不需要根据myVector中元素的类型改变，自动推断变量类型
for (auto it : v) {//修改it时只会影响副本元素，不会修改原容器v的元素
	cout << it << " ";
}
for	(auto &it : v){//&引用可以修改原容器v的元素
    cout << it << " ";
}
```

```cpp
//通过下标
for	(int i = 0;i < v.size();i++){
    cout << v[i] << " ";
}
```



### 动态二维数组

> 例如当1 <= n,m <= 1e6,而n*m <= 1e6;
> 无法直接构建arr[n] [m],需要使用动态数组

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
const int N = 100005;
vector<int>v[N];//v[0]={},v[1]={},v[2]={}...

int main() {
	int n = 9;
	for (int i = 1; i <= n;i++) {
		v[i].emplace_back(0);//如果需要让数组下表从1开始，则需要填充第一位
		for (int j = 1; j <= n;j++) {
			v[i].emplace_back(i*j);
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cout  << left << setw(3)<< v[i][j] << ' ';
		}puts("");
	}


	return 0;
}
```



```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using  namespace std;
vector<vector<int>>v;//V = {v1,v2,v3...}
vector<vector<int>>dp(n+1,vector<int>(26,INF));//v[n+1][26]每个元素初始化为INF
//vector dp(n + 1, vector<int>(n + 1, 1e9));  //c++17
int main() {
	//构建一个arr[n][m];的动态二维数组
	int n, m; cin >> n >> m;
	for (int i = 0; i < n; i++) {
		vector<int>v1;
		for (int j = 0; j < m; j++) {
			int x; cin >> x;
			v1.push_back(x);
		}
		v.push_back(v1);
	}

	for (int i = 0; i < v.size(); i++) {
		for (int j = 0; j < v[i].size(); j++) {
			cout << v[i][j] << ' ';
		}puts("");
	}
}
```



------





## queue

> 队列是一种先进先出（FIFO）的数据结构，元素按照其被添加的顺序进行处理。



### 常用函数

| 常用函数  |                    |
| --------- | ------------------ |
| q.push(x) | 在队尾插入元素x    |
| q.pop(x)  | 删除队首元素       |
| q.size()  | 返回队列中元素个数 |
| q.empty() | 返回队列是否为空   |
| q.front() | 返回队首元素       |
| q.back()  | 返回队尾元素       |
|           |                    |



### 定义及初始化

queue<Type, Container> 	// (<数据类型，容器类型>）
初始化时必须要有数据类型，容器可省略，省略时则默认为[deque](https://so.csdn.net/so/search?q=deque&spm=1001.2101.3001.7020) 类型

```cpp
//queue的定义  例
queue<int>q1; //定义一个储存数据类型为int的queue容器q1 
queue<double>q2; //定义一个储存数据类型为double的queue容器q2
queue<string>q3; //定义一个储存数据类型为string的queue容器q3
queue<结构体类型>q4; //定义一个储存数据类型为结构体类型的queue容器q4
```



### 清空

> queue没有clear()函数；可以通过以下方式清空队列

```cpp
queue<int>q;
//方法一
q = queue<int>();
//方法二
queue<int>empty;
swap(q,empty);
//方法三
while(q.size()) q.pop();
```



### 元素访问

queue队列的元素只能访问队首元素或队尾元素，通过.pop()每次将队首元素弹出后遍历队列

```cpp
queue<int>q;
for (int i = 0; i < 10;i++) {
	q.push(i*10);
}
for (int i = 0; i < 5;i++) {
	cout << q.front() << ' ';
	q.pop();
}
```





### 优先队列

每次元素入队后会按一定次序排列元素，只能访问队首元素，**默认大根堆**

| 常用函数   |                  |
| ---------- | ---------------- |
| pq.push(x) | 向队列插入元素x  |
| pq.pop()   | 弹出队首元素     |
| pq.top()   | 返回队首元素     |
| pq.size()  | 返回队列元素个数 |
| pq.empty() | 返回队列是否为空 |



> priority_queue<结构类型> 队列名;
> priority_queue<double>q0;
> priority_queue<int,vector<int>,less<int> >q1;  			//大根堆，父节点>子节点
> priority_queue<int, vector<int>, greater<int>> q2;  	//小根堆 ，父节点<子节点

```cpp
//例	利用大根堆实现元素自动从大到小排列
#include <iostream>
#include <queue>
using namespace std;
priority_queue<int>q;
int main() {
	for (int i = 0;i < 5;i++){
		int x; cin >> x;
		q.push(x);
	}
	while (q.size()){
		cout << q.top();
		q.pop();
	}
	return 0;
}
```



```cpp
///结构体重载<运算符
struct Edge{
	int s,x,y;
	bool operator < (const Edge &e)const {
		return s > e.s;//小根堆，堆顶为最小值
        //return s < e.s;//大根堆，堆顶为最大值
	}
};

priority_queue<Edge>pq;
```





------





## deque

双端队列容器，速度慢，能通过下标访问元素，对队首/队尾操作较快

### 常用函数

| 常用函数        |                                                              |
| --------------- | ------------------------------------------------------------ |
| front()         | 返回第一个元素的引用。                                       |
| back()          | 返回最后一个元素的引用。                                     |
| assign()        | 用新元素替换原有内容。                                       |
| push_back()     | 在序列的尾部添加一个元素。O(1)                               |
| push_front()    | 在序列的头部添加一个元素。O(1)                               |
| pop_back()      | 移除容器尾部的元素。O(1)                                     |
| pop_front()     | 移除容器头部的元素。O(1)                                     |
| insert()        | 在指定的位置插入一个或多个元素。  O(n)                       |
| erase()         | 移除一个元素或一段元素。O(n)                                 |
| clear()         | 移出所有的元素，容器大小变为 0。                             |
| swap()          | 交换两个容器的所有元素。                                     |
| emplace()       | 在指定的位置直接生成一个元素。                               |
| emplace_front() | 在容器头部生成一个元素。和 push_front() 的区别是，该函数直接在容器头部构造元素，省去了复制移动元素的过程。 |
| emplace_back()  | 在容器尾部生成一个元素。和 push_back() 的区别是，该函数直接在容器尾部构造元素，省去了复制移动元素的过程。 |



### 定义及初始化

```cpp
//1) 创建一个没有任何元素的空 deque 容器：
deque<int>d1;

//)2 创建一个具有 10 个元素的 deque 容器，其中每个元素都采用对应类型的默认值：
deque<int>d2(10,-1);	//int类型初始化为-1,第二个参数不填则默认为0

//)3 创建一个具有 10 个元素的 deque 容器，并为其初始化
deque<string>d3(10,"abc");

//)4 拷贝构建
deque<int> d4(d1);
```







------



## list

> 双向循环链表容器,不支持通过下标访问元素，插入删除时间复杂度都为O(1)
>
> 访问效率效率低 O(n)
>
> //迭代器不可用NULL判空，如if(it == NULL)为非法判断
> //可以将其指向end(),再利用end()判断

### 常用函数

| 常用函数           |                                                              |
| ------------------ | ------------------------------------------------------------ |
| push_back/front(x) | 将元素x插入容器末尾 /队首 O(1)                               |
| pop_back/front()   | 删除末尾/队首元素  O(1)                                      |
| insert(it,x)       | 在迭代器it前一个位置插入元素x    O(1)                        |
| erase()            | 移除迭代器first(到last之间)的元素, 删除后迭代器失效          |
| size()             | 返回容器元素个数                                             |
| empty()            | 返回容器是否为空                                             |
| clear()            | 清空容器                                                     |
| front()/back()     | 返回队首/末尾元素                                            |
| begin()            | 返回指向容器开始的迭代器                                     |
| end()              | 返回指向容器末尾的迭代器,解引用后为容器大小,next(end())又循环为begin() |





### 遍历链表

> queue<int>q;

```cpp
//利用迭代器
for (list<int>::iterator it = q.begin(); it != q.end(); it++) {
	cout << *it << " ";
}
```



```cpp
//fou(auto& i:q)   c++11
for (int& i:l){
	cout << i << ' ';
}
```



**二维链表**

```cpp
#include <iostream>
#include <list>

void dfs(vector<list<int>>&q,int u){
    for(auto& k:q[u]){
        cout << k << endl;
    }
}

int n;
vector<list<int>>q(n+1);
dfs(q,1);
```







------

## stack

栈，先进后出

### 常用函数

| 常用函数   |                      |
| ---------- | -------------------- |
| sk.push()  | 插入一个元素         |
| sk.pop()   | 弹出栈顶元素         |
| sk.top()   | 返回栈顶元素         |
| sk.size()  | 返回元素个数         |
| sk.empty() | 返回栈中元素是否为空 |



### 清空

由于stack没有clear()函数，可以手动清空，或者sk = stack<int>();



### 例

```cpp
#include <iostream>
#include <stack>
using namespace std;
stack<int>p;
int main() {
	for (int i = 0; i < 5;i++) {
		int x; cin >> x;//1 2 3 4 5
		p.push(x);
	}
	for (int i = 0; i < 5;i++) {
		cout << p.top();//54321
		p.pop();
	}
	return 0;
}
```





------



## set

set是以rb_tree为底层机构，因此有元素自动排序的特性。元素不能直接被改变

> set	不可存在重复的数



### 常用函数

| set<int>q          |                                                              |
| ------------------ | ------------------------------------------------------------ |
| insert()/emplace() | 插入一个数                                                   |
| find()             | O(logn)查找一个数,返回这个数的迭代器,不存在则返回end()地址   |
| erase()            | 根据参数，删除一个数x/一个迭代器it/两个迭代器[it1,it2)之间的值 |
| empty()            | 判断容器是否为空                                             |
| size()             | 返回当前容器元素个数                                         |
| clear()            | 删除容器中所有元素                                           |
| begin()            | 返回指向容器第一个元素的迭代器                               |
| end()              | 返回指向容器末尾元素的迭代器，解引用后为容器元素个数         |
| q.lower_bound(x)   | 返回第一个大于等于x的迭代器O(logn),不要使用lower_bound(last,end,x)会退化为O(N) |
| q.upper_bound(x)   | 返回第一个大于x的迭代器                                      |
| equal_range()      | 返回元素值为n的区间(pair类型) //*a.equal_range().first和 *a.equal_range()second之间 |





### 例

```cpp
#include <iostream>
#include <set>
using namespace std;
set<int>p;
int main() {
	for (int i = 0; i < 5;i++) {
		int x; cin >> x;
		p.insert(x);
	}
	/*cout << *p.lower_bound(2) << endl;
	cout << *p.upper_bound(2) << endl;*/
	cout << *p.equal_range(2).first;
	cout << *p.equal_range(2).second;
	
	for (auto& it= p.begin();it != p.end();it++) {//通过迭代器遍历
		cout << *it << endl;//*号解引用
	}
	p.erase(p.begin(), p.end());

	return 0;
}
```





### 重载

```cpp
//重载为降序
struct cmp{
	bool operator () (const int &e1,const int &e2)const{
		return e1 > e2;
	}
};

set<int,cmp>se;
```





```cpp
//结构体重载
struct Edge{
	int a,b;
	bool operator < (auto &e2)const{
        return a < e2.a;//升序
        //return a > e2.a;//降序
	}
};
set<Edge>se;
```



### multiset

> 可以存在重复的数

multiset中count(x)时间复杂度为O(k+log(N))   ，其中k为元素x出现的次数，N为集合大小

multiset.erase(x);会把所有的x删除，诺只想要删一个，则应删除迭代器



### unordered_set

> #include <unordered_set>
>
> 与set唯一的区别就在于 unordered_set 容器不会自行对存储的数据进行排序 





------



## bitset

每位只占1bite空间，支持各种位运算如

~	|	&	^	<<	>>	[ ]	==	!= 等




### 常用函数

| 常用函数          |                                                              |
| ----------------- | ------------------------------------------------------------ |
| size()            | 返回长度                                                     |
| count()           | 返回位值为1的数量                                            |
| set()             | 无参则将所有位设为1，一个参数则将下标为pos设为1，两个参数则将下标为pos的位设为k |
| reset()           | 无参将所有位设为0，一个参数则将下标为pos的位设为0            |
| flip()            | 无参则将所有位取反，一个参数则将下标为pos的位取反            |
| all()             | 是否所有位都是1                                              |
| none()            | 是否所有位都是0                                              |
| any()             | 是否至少有一个1                                              |
| b.to_string()     | 返回为字符串型                                               |
| b.to_ulong()      | 返回为无符号整型  to_ullong为长整型                          |
| b._Find_first()   | 返回第一个1的位置，如果没有则返回b.size()                    |
| b._Find_next(pos) | 返回pos后面第一个1的位置，如果没有则返回b.size()             |
| `<<` `&` `|` `^`  | 支持`&` `|` `^`  和移位操作                                  |



### 初始化

```cpp
bitset<31>b = n;			//int n 转二进制,b[0]~b[30]为二进制低位到高位,cout<<b;为高位到低位
bitset<N> bitset1; 			// 创建一个长度为 N 的 bitset，所有位默认初始化为 0
bitset<N> bitset2(value); 	// 使用二进制整数 value 初始化一个长度为 N 的 bitset //无符号整数
bitset<N> bitset3(string); 	// 使用二进制字符串 string 初始化一个长度为 N 的 bitset//只含'0'或'1'   //bitset<N>b3(string("00110101"));
bitset<N> bitset4(bitset); 	// 使用另一个 bitset 初始化一个长度为 N 的 bitset
```



```cpp
bitset<32>b;

int n = 127;//int b = 0b111111;
b = n;//使用整型

string s = "111111";
b = bitset<32>(s);//使用二进制字符串(构造函数)
//bitset<32>b("111111");
```





```cpp
bitset<N>dp[N];//运算效率比int[][]数组高

for(int i = 1;i <= n;i++){
    int a,b;cin >> a >> b;
    dp[a][b] = 1;
}
for(int i = n;i >= 1;i--){
    dp[i] |= dp[i+c[i]];
    ans = max(ans,dp[i].count());
}
```





------



## iomanip

### 常用函数

| 常用函数          |                              |
| ----------------- | ---------------------------- |
| fixed             | 固定以浮点数形式输出         |
| setprecision(n)   | 保留n位小数                  |
| setw(n)           | 设置位宽为n                  |
| left     right    | 左/右对齐                    |
| setfill(c)        | 以字符c填充位宽空位          |
| `dec` `oct` `hex` | 以10进制，8进制，16进制输出  |
| setbase(n)        | 以n进制输出   n只能为10,8,16 |



### setprecision

> 用于设置浮点数精度

//超过对应数据类型范围仍然会掉精度

```cpp
double n = 1.145141919810;
cout <<fixed << setprecision(6) << n << endl;
//将a四舍五入到n位，不足n位则会自动添0（如果n为整型，n*1.0即可）

cout << 1.1 << endl;//会对后续其它浮点数输出会造成影响	
cout << defaultfloat << 1.1 << endl;//defaultfloat可以取该影响
cout << 1.1 << endl;
```

```cpp
double a = 1.1234567;
a = (int)(1000.0 * a + 0.5) / 1000.0;//保留3位小数，四舍五入，根据需要增删0
```

```c
//c语言自定义保留n位小数，四舍五入
#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    printf("%.*f",n,123.666666);
}
```





### setw

> 设置	默认右对齐

```cpp
int a = 1, b = 12, c = 123;
cout << setw(4) << a << endl;
cout << setw(4) << b << endl;
cout << setw(4) << c << endl;
```





### 对齐

> left  	//输出左对齐
> right	//输出右对齐

```cpp
for (int i = 0;i <5;i++){
    cout << setw(5) << left << i;
}
```





### setfill

> 字符c

```cpp
string s = "abcde";
cout << setfill('*') <<setw(10)<< s << endl;
```





------

## numeric

### 常用函数

| 常用函数                           |                                                              |
| ---------------------------------- | ------------------------------------------------------------ |
| accumulate(begin,end,value)        | 将区间内的元素与初始值想加，返回他们的和(返回值类型与value相同) |
| partial_sum(begin,end,res)         | 区间前缀和，并将结果写入res                                  |
| adjacent_difference(begin,end,res) | 区间差分                                                     |
| iota(begin,end,value)              | 以value为初始值，批量递增赋值                                |





### accumulate

accumulate(first,last,value)

```cpp
const int N = 1e9;
vector<int>a = {N,N,N,3,1,5,7,5,4};
long long sum = accumulate(a.begin(),a.end(),0LL);//需要注意溢出问题
```





### partial_sum

求前缀和函数

partial_sum(first,last,res)    区间求前缀和并将结果写入res

```cpp
vector<int>a = {2,6,8,3,1,5,7,5,4},b(3);
partial_sum(a.begin(),a.end(),b.begin());//b = 2 8 16
partial_sum(a.begin(),a.end(),a.begin());//原地求前缀和
```



### adjacent_difference

差分函数，与前缀和写法类似



### iota

iota(begin,end,value)   将 [bg,ed) 中的元素依次赋值为 val,val+1,val+2,⋯，复杂度 O(N)。

```cpp
//用于原地初始化并查集
int a[100],n = 10;
iota(a+1,a+n+1,1);//a = 0,1,2,3,4,5,6,7,8,9,10
```







------

## sstream

多次使用同一个stringstream对象，每次使用后都需要对其进行清空，**既要清空其内容，又要清空其状态**



### 定义及初始化

```cpp
stringstream ss;	//定义
ss.clear();			//清空状态，仅仅清空标志位，并没有释放内存
ss.str("");			//初始化为空串，清除stringstream内容
ss.str(s);			//以字符串s初始化ss
ss.str();			//转化为string类型，cout << ss.str() << endl;
ss.fail();			//返回ss是否输入成功
```

```cpp
#include <iostream>
#include <sstream>
using namespace std;

int main(){
	stringstream ss;
	string s = "111 222";
	int a,b,c;
	ss << s;
	ss >> a >> b;  //返回值为ss.fail(),ss已经为空,返回1
	
	ss.clear();//需要清空ss的状态才能继续使用
	ss << "333";
	ss >> c;

	cout << a << " " << b << " " << c << endl;
}
```



### 例

```cpp
//例：输入第一行一个数字N，接下来N行数据，每一行数据为个数不确定的整数。将每行的总和输出出來
#include <iostream>
#include <sstream>
using namespace std;

int main(){
	int tt;cin >> tt;
	stringstream ss;
	getchar();//忽视第一个n后的回车
	while(tt--){
		string s;
		getline(cin,s);//getline(cin,s,'\n');默认以回车作为结束符
		int ans = 0,x = 0;

		ss.clear();
		ss.str(s);  //或ss << s;

		while(ss >> x){
			ans += x;
		}
		cout << ans << endl;
	}
}
```

```cpp
//例：分割单词
#include <iostream>
#include <sstream>
using namespace std;

int main(){
	string s;
	stringstream ss;
	while(getline(cin,s)){//以EOF结束
		ss.clear();
		ss << s;
		string word;
		while(ss >> word){
			cout << word << endl;
		}
	}
}
```



------

## tuple

#include <tuple>

tuple（元组）在c++11开始引用，是一个固定大小的不**同类型值的集合**，是**泛化的std::pair**。我们也可以把他当做一个通用的结构体来用，不需要创建结构体又获取结构体的特征，在某些情况下可以取代结构体使程序更简洁，直观。std::tuple理论上可以有无数个任意类型的成员变量，而std::pair只能是2个成员，因此在需要保存3个及以上的数据时就需要使用tuple元组了。



### 声明



```cpp
tuple<int,string,char,bool> t;
```



### 元素访问

> `get<idx>(t)`  //访问元组t中的第idx个元素（从0开始）

```cpp
//get<Idx>()引用访问，其中idx不能用变量替代,如i,j,k等
cin >> get<0>(t);
cout << get<0>(t) << endl;
```

```cpp
//c++17 结构化绑定访问
for_each(t+1,t+n+1,[&](auto &x){auto &[a,b,c,d] = x;cin >> a >> b >> c >> d;});
for(int i = 1;i <= n;i++){
    auto &[num,name,sex,st] = t[i];
    cout << name << ' ' << num << ' ' << sex << ' ' << st << endl;
}

for(int i = 1;i <= n;i++){
    auto &[num,name,sex,st] = t[i];
    cout << name << ' ' << num << ' ' << sex << ' ' << st << endl;
}
```



### tie

**可以用于解包pair、tuple**

引用参数为引用效果

```cpp
int a = 10,b = 20,c = 30,d = 40;
tie(a,b,c,d) = make_tuple(b,a,d,c);//a = 20,b = 10,c = 40c,d = 30;
//tie(a,b) = make_pair(b,a+b); //可以用来递推求斐波那列
//tie(a,b) = pair{b,a+b};
//性能不太好
pair<int,int>p = {333,666};
tie(a,b) = p;//a = 333,b = 666;
```





**可以用于为结构体引入字典序比较**

```cpp
struct Edge{
	int n,k;
	string s;
	bool operator < (auto &e){
		return tie(n,s,k) < tie(e.n,e.s,e.k);
	}
};

int main(){
	Edge e1 = {12,"abc",56};
	Edge e2 = {12,"abd",56};
	if(e1 < e2){cout << "YES";}
	else cout << "NO";
}
```





------



## ctime

### clock_t

```cpp
//计算程序运行某一段的耗时(ms)
//例1
#include <iostream>
#include <ctime>
using namespace std;
clock_t start1, end1, start2, end2;
int main() {	
	start1 = clock();
	for (int i = 0; i < 5e8; i++){
		int b; b = i;
	}
	end1 = clock() - start1;
	cout << end1 << "ms" << endl;

	start2 = clock();
	for (int i = 0; i < 1e9; i++){
		int b; b = i;
	}
	end2 = clock();
	cout << end2 - start2 << "ms" << endl;
}
```

```cpp
//例2
#include <iostream>
using namespace std;
int main() {
	int start1 = clock();
	for (int i = 0; i < 1e7; i++);
	int end1 = clock();
	cout << end1 - start1 << "ms" << endl;

	int start2 = clock();
	for (int i = 0; i < 1e9; i++);
	int end2 = clock();
	cout << end2 - start2 << "ms" << endl;

	return 0;
}
```





------





## 扩展库ext

[libstdc++: detail Directory Reference (gnu.org)](https://gcc.gnu.org/onlinedocs/gcc-14.1.0/libstdc++/api/dir_b225f7c1a7cba6a81c0d5e94468925c3.html)

```cpp
#include <bits/extc++.h>				//扩展库万能头

#include <ext/pb_ds/assoc_container.hpp> //关联容器
#include <ext/pb_ds/hash_policy.hpp>     //哈希表
#include <ext/pb_ds/tree_policy.hpp>     //平衡树
#include <ext/pb_ds/trie_policy.hpp>     //字典树
#include <ext/pb_ds/priority_queue.hpp>  //堆
using namespace __gnu_pbds;
```



### 关于pb_ds

pb\_ds 库全称 Policy-Based Data Structures。
pb\_ds 库封装了很多数据结构，比如哈希（Hash）表，平衡二叉树，字典树（Trie 树），堆（优先队列）等。
就像 `vector`、`set`、`map` 一样，其组件均符合 STL 的相关接口规范。部分（如优先队列）包含 STL 内对应组件的所有功能，但比 STL 功能更多。
pb\_ds 只在使用 libstdc++ 为标准库的编译器下可以用。
可以使用 `begin()` 和 `end()` 来获取 `iterator` 从而遍历
可以 `increase_key`,`decrease_key` 以及删除单个元素









### hash

```cpp
#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/hash_policy.hpp>
using namespace __gnu_pbds;
```



#### 定义

```cpp
gp_hash_table<string,bool> hs;//探测法（稍微快一点
cc_hash_table<string,bool> hs;//拉链法
```



操作和map类似，支持[ ]和find( )操作



#### 例

```cpp
//例：字符串哈希  https://www.luogu.com.cn/problem/U461211
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/hash_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

int main(){
	gp_hash_table<string,bool>hs;
	int n,ans = 0;cin >> n;
	while(n--){
		string s;cin >> s;
		if(hs.find(s) == hs.end()) hs[s] = 1,ans++;
	}
	cout << ans;
}
```







### tree

pb_ds里的tree都是平衡树，一般使用`rb_tree_tag`红黑树，性能较好，元素有序不可重
```cpp
#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
```



#### 定义

> tree<`Key`,`Mapped`,`Cmp_Fn`,`Tree_Tag`,`Node_Update`>tr
>
> `Key` ：储存的**元素类型**，如int,pair,sturct等,并配合lower_bound和upper_bound成员函数查找
>
> `Mapped` ：映射规则：[集合][类似set](则此处填**null_type**，低版本g++填null_mapped_type)，[带值集合][类似map](此处填类似于map<Key,Value>的**Value类型**)
>
> `Cmp_Fn` ：关键字的**比较函数**，例如`less<Key>`从小到大
>
> `Tree_Tag`：使用何种**底层数据结构类型**，默认是红黑树`rb_tree_tag`
>
> `Node_Update` ： 用于更新**节点的策略**，默认`null_node_update`，若要使用求排名`order_of_key` 和 找k小值`find_by_order` 方法，需要使用 `tree_order_statistics_node_update`

```cpp
tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update>rb;
```





#### 常用函数

| 常用函数             |                                                   |
| -------------------- | ------------------------------------------------- |
| rb.insert(x);        | 插入x                                             |
| rb.erase(x);         | 删除x                                             |
| rb.lower_bound(x);   | 返回第一个大于等于x的迭代器                       |
| rb.upper_bound(x);   | 返回第一个大于x的迭代器                           |
| rb.order_of_key(x);  | 求x的排名(下标从0开始)                            |
| rb.find_by_order(x); | 求第x小的值(下标从0开始)                          |
| rb.join(rb2);        | 将rb2合并进rb，前提是两棵树类型一样且没有重复元素 |
| rb.split(x,rb2);     | 分裂，key小于等于x的元素属于rb，其余的属于rb2     |







#### 例

```cpp
//例：普通平衡树 https://www.luogu.com.cn/problem/P3369
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

int main(){
	tree<int,null_type,less_equal<int>,rb_tree_tag,tree_order_statistics_node_update>rb;
	//less_equal 或 使用pair<int,int>+umap时间戳，使得能存在相同key
	int n;cin >> n;
	for(int i = 1;i <= n;i++){
		int op,x;cin >> op >> x;
		if(op == 1) rb.insert(x);//插入x(有重复x)
		if(op == 2) rb.erase(rb.upper_bound(x));//删除x(只删除一个)
		if(op == 3) cout << rb.order_of_key(x)+1 << '\n';//查询x的排名(树中下标从0开始，结果要+1)
		if(op == 4) cout << *rb.find_by_order(x-1) << '\n';//查询排名为x的值(同上,查询时要-1)
		if(op == 5) cout << *(--rb.upper_bound(x)) << '\n';//查询x的前驱(小于x的最大值)
		if(op == 6) cout << *rb.lower_bound(x) << '\n';//查询x的后继(大于x的最小值)
	}
}
```

```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
using pii = pair<int,int>;
unordered_map<int,int>mp;

int main(){
	tree<pii,null_type,less<pii>,rb_tree_tag,tree_order_statistics_node_update>rb;

	int n;cin >> n;
	for(int i = 1;i <= n;i++){
		int op,x;cin >> op >> x;
		if(op == 1) rb.insert({x,mp[x]++});//插入x(有重复x，先插入再++)
		if(op == 2) rb.erase(rb.lower_bound({x,--mp[x]}));//删除x(只删除一个，先--再删除)
		if(op == 3) cout << rb.order_of_key({x,0})+1 << '\n';//查询x的排名(树中下标从0开始，结果要+1)
		if(op == 4) cout << rb.find_by_order(x-1)->first << '\n';//查询排名为x的值(同上,查询时要-1)
		if(op == 5) cout << (--rb.lower_bound({x,0}))->first << '\n';//查询x的前驱(小于x的最大值)
		if(op == 6) cout << rb.upper_bound({x,mp[x]})->first << '\n';//查询x的后继(大于x的最小值)
	}
}
```







### 堆

```cpp
#include <ext/pb_ds/priority_queue.hpp>
using namespace __gnu_pbds;
```



#### 定义

```cpp
__gnu_pbds::priority_queue<int,greater<int>> pq;
//要注明命名空间，防止与std冲突
//第二个参数不写则默认大根堆
//第三个tag参数不写默认为配对堆pairing_heap_tag，性能较好
```

| 不同tag性能比较                            | push                                    | pop                                     | modify                                  | erase                                   | Join              |
| ------------------------------------------ | --------------------------------------- | :-------------------------------------- | --------------------------------------- | --------------------------------------- | ----------------- |
| `pairing_heap_tag`<br />配对堆             | $O(1)$                                  | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | $O(1)$            |
| `binary_heap_tag`<br />二叉堆              | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | $\Theta(n)$                             | $\Theta(n)$                             | $\Theta(n)$       |
| `binomial_heap_tag`<br />二项堆            | 最坏 $\Theta(\log(n))$ 均摊 $O(1)$      | $\Theta(\log(n))$                       | $\Theta(\log(n))$                       | $\Theta(\log(n))$                       | $\Theta(\log(n))$ |
| `rc_binomial_heap_tag`<br />冗余计数二项堆 | $O(1)$                                  | $\Theta(\log(n))$                       | $\Theta(\log(n))$                       | $\Theta(\log(n))$                       | $\Theta(\log(n))$ |
| `thin_heap_tag`<br />简化的斐波那契堆      | $O(1)$                                  | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | 最坏 $\Theta(\log(n))$ 均摊 $O(1)$      | 最坏 $\Theta(n)$ 均摊 $\Theta(\log(n))$ | $\Theta(n)$       |





#### 常用函数

| 常用函数         |                                                              |
| ---------------- | ------------------------------------------------------------ |
| pq.push(x);      | 插入x,会返回一个指向x所在位置的`__gnu_pbds::priority_queue<...>::point_iterator`的点类型迭代器 |
| pq.pop();        | 弹出堆顶元素                                                 |
| pq.top();        | 返回堆顶元素                                                 |
| pq.modify(it,x); | 将点迭代器it位置的键值改为x，会返回一个点迭代器，并对底层存储结构排序 |
| pq.erase(it);    | 把点迭代器it所在位置的键值从堆中擦除                         |
| pq.join(pq2);    | 把堆pq2并入到堆pq，并清空pq2。                               |
| pq.size();       | 返回元素个数                                                 |
| pq.empty();      | 返回是否为空                                                 |

对于不同的tag参数，其底层实现并不相同，点迭代器的失效条件也不一样。可能在pop或erase后，点迭代器依然不会失效。

不支持直接获取堆顶的点迭代器，在push或modify操作时获取。对迭代器begin()解引用后也并不等于top()。

无法通过点迭代器合并堆，也无法仅凭点迭代器找到所属堆进行合并，必须显示持有目标堆的引用。



#### 例

[P3377 【模板】左偏树/可并堆 - 洛谷 (luogu.com.cn)](https://www.luogu.com.cn/problem/P3377)

```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_pbds;
using pii = pair<int,int>;
const int N = 100005;
int n,q,p[N];
bool st[N];
__gnu_pbds::priority_queue<pii,greater<pii>> pq[N];

int find(int x){
	if(p[x] != x) p[x] = find(p[x]);
	return p[x];
}

int main(){
	cin >> n >> q;
	for(int i = 1;i <= n;i++){ p[i] = i; }
	for(int i = 1;i <= n;i++){
		int x;cin >> x;
		pq[i].push({x,i});
	}

	while(q--){
		int op;cin >> op;
		if(op == 1){//将第a个数和第b个数所在堆合并,诺已被删除或已经在同一个堆则无视该操作
			int a,b;cin >> a >> b;
			int pa = find(a),pb = find(b);
			if(st[a] || st[b] || pa == pb) continue;
			pq[pa].join(pq[pb]);
			p[pb] = pa;
		}
		else{//输出第a个数所在堆的最小数,然后将最小数删除(诺有多个最小数,优先删除先输入的)。
            //诺第a个数已经被删除,输出-1,并无视删除操作。
			int a;cin >> a;
			if(st[a]) {cout << -1 << '\n';continue;}

			int pa = find(a);
			st[pq[pa].top().second] = 1;
			cout << pq[pa].top().first << '\n';
			pq[pa].pop();
		}
	}
}
```



[P11266 【模板】可并堆 2 - 洛谷 (luogu.com.cn)](https://www.luogu.com.cn/problem/P11266)

维护序列a[n]，和n和集合s[n]，初始时s[i] = i

- `0 x y`：表示将元素 $y$ 从集合 $S_x$ 中删去。保证此时元素 $y$ 在集合 $S_x$ 中。
- `1 x`：表示询问 $\min_{i\in S_x} a_i$，保证此时集合 $S_x$ 非空。
- `2 x y`：将集合 $S_y$ 中并入 $S_x$ 并清空集合 $S_y$。保证此时集合 $S_x,S_y$ 均非空，且此次操作后不会再出现涉及集合 $S_y$ 的操作。
- `3 x y z`：表示将 $a_y$ 赋值为 $z$。保证此时元素 $y$ 在集合 $S_x$ 中，且 $z<a_y$。

```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
const int N = 1000006;
__gnu_pbds::priority_queue<int,greater<int>> pq[N];
__gnu_pbds::priority_queue<int,greater<int>>::point_iterator it[N];

int main() {
	int n,q;cin >> n >> q;
	for(int i = 1;i <= n;i++){
		int x;cin >> x;
		it[i] = pq[i].push(x);
	}
	while(q--){
		int op,x,y,z;cin >> op;
		if(op == 0){
			cin >> x >> y;
			pq[x].erase(it[y]);
		}
		if(op == 1){
			cin >> x;
			cout << pq[x].top() << '\n';
		}
		if(op == 2){
			cin >> x >> y;
			pq[x].join(pq[y]);
		}
		if(op == 3){
			cin >> x >> y >> z;
			pq[x].modify(it[y],z);
		}
	}
}
```





### trie

字典树，功能较少，不能满足大多数需求



```cpp
#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/trie_policy.hpp>
```



#### 定义

```cpp
trie<string,null_type,trie_string_access_traits<>,pat_trie_tag,trie_prefix_search_node_update> tr;
```





#### 常用函数

| 常用函数                     |                                                              |
| ---------------------------- | ------------------------------------------------------------ |
| tr.insert(s);                | 插入字符串s                                                  |
| tr.erase(s);                 | 删除字符串s                                                  |
| tr.join(tr2);                | 将tr2并入tr                                                  |
| auto p = tr.prefix_range(s); | 查询以s为前缀的字符串有哪些，p为两个迭代器pair<tr::iterator , tr::iterator> |



#### 例

```cpp
//https://www.luogu.com.cn/problem/P8306
//求 S1∼SN 中 T 是多少个字符串的前缀
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/trie_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

void sol(){
	trie<string,null_type,trie_string_access_traits<>,pat_trie_tag,trie_prefix_search_node_update> tr;
	int n,q;cin >> n >> q;
	for(int i = 1;i <= n;i++){
		string s;cin >> s;
		tr.insert(s);
	}
	while(q--){
		string s;cin >> s;
		auto p = tr.prefix_range(s);
		int ans = 0;
		for(auto it = p.first;it != p.second;it++){//时间复杂度为O(N*ans),并不能通过本题
			//cout << *it << endl;
			ans++;
		}
		cout << ans << '\n';
	}
}

int main(){
	int T;cin >> T;
	while(T--){sol();}
}
```







/



### rope

STL 中的 `rope` 也起到**块状链表**的作用，它采用可持久化平衡树实现，可完成随机访问和插入、删除元素的操作，可以在O(1)的时间拷贝历史版本

由于 `rope` 并不是真正的用块状链表来实现，所以它的时间复杂度并不等同于块状链表，而是相当于可持久化平衡树的复杂度（即 $O(\log n)$），但常数较大，空间需求较大，可以维护的东西较少

```cpp
#include <ext/rope>
using namespace __gnu_cxx;
```





#### 定义

与vector等容器类似，不可直接赋值，应用push_back、replace、insert等修改元素

```cpp
rope<int>r;
```



#### 常用函数

| 常用函数                                                     |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| r.push_back(x)    r.append(x)                                | 在末尾添加元素x。空间复杂度O(log n)， 时间复杂度O(1)         |
| r.pop_back()                                                 | 删除末尾元素。时间复杂度O(log n)，时间复杂度O(1)             |
| r.insert(pos,x)                                              | 在pos位置前插入元素x，时间复杂度O(log n + len)，空间复杂度O(len)，len 为插入内容大小 |
| r.erase(pos,len)                                             | 删除pos位置起，len个元素， 时间复杂度O(log n + len)          |
| r.at(x)      r[x]                                            | 访问a的第x个元素，时间复杂度O(log n)                         |
| r.size()    r.length()                                       | 获取r的大小                                                  |
| lower_bound(begin,end,x)                                     | 二分查找$O(log^2n)$                                          |
| r.substr(begin,end)                                          | 截取子段 [ begin , end )，时间复杂O(log n + len)，空间复杂度O(len) |
| r.replace(i, len, r2)<br />r.replace(i, len, s)<br />r.replace(i, len, cnt, c) | 将i位置开始长度为len个元素删掉，替换为r2/c风格字符串s/cnt个字符c。<br />时间复杂度为 $O(\log{n}) + m$，其中m为新插入内容的长度。 |



#### 例

```cpp
//数列分块入门6(元素插入和删除)  https://loj.ac/p/6282
#include <iostream>
#include <ext/rope>
using namespace std;

int main(){
	__gnu_cxx::rope<int>a;
	int n;cin >> n;
	for(int i = 1;i <= n;i++){
		int x;cin >> x;
		a.push_back(x);
	}
	while(n--){
		int op,l,r,c;cin >> op >> l >> r >> c;
		if(op == 0){//在第l个数字前插入r
			a.insert(l-1,r);
		}
		else{//询问第r个数字的值
			cout << a[r-1] << '\n';
		}
	}
}
```



```cpp
//文艺平衡树(区间翻转)   https://www.luogu.com.cn/problem/P3391
#include <bits/stdc++.h>
#include <ext/rope>
using namespace std;
using namespace __gnu_cxx;
int n,m;
rope<int>a,b;

rope<int> sub(rope<int>&v,int l,int r){
	return v.substr(v.begin()+l,v.begin()+r);
}

int main(){
	cin >> n >> m;
	for(int i = 1;i <= n;i++){
		a.push_back(i); b.push_back(n-i+1);
	}
	while(m--){
		int l,r;cin >> l >> r;//将区间l~r翻转
		if(l >= r) continue;
		auto tmp = sub(a,l-1,r);
		a = sub(a,0,l-1) + sub(b,n-r,n-l+1) + sub(a,r,n);
		b = sub(b,0,n-r) + tmp + sub(b,n-l+1,n);
	}
	for(int i = 0;i < n;i++){ cout << a[i] << ' '; }
}
```



```cpp
//高级打字机(数据可持久化)  https://www.luogu.com.cn/problem/P1383
#include <bits/stdc++.h>
#include <ext/rope>
using namespace std;
using namespace __gnu_cxx;
const int N = 100005;
rope<char>a[N],now;//a[]存历史版本，now为当前版本
int cnt;

int main(){
	int q;cin >> q;
	while(q--){
		char op;cin >> op;
		if(op == 'T'){ //在文章末尾添加一个小写字母x
			char x;cin >> x;
			now.append(x);
			a[++cnt] = now;
		}
		else if(op == 'U'){ //撤销最后x次修改操作
			int x;cin >> x;
			now = a[cnt-x];
			a[++cnt] = now;
		}
		else{
			int x;cin >> x; //输出当前文章中第x个字母(本操作不算修改操作)
			cout << now[--x] << '\n';
		}
	}
}
```



































