# espprc_python_API
脉冲算法的C++实现，原始C++代码地址https://github.com/DouYishun/vrp-espprc
用SWIG进行一个简易封装，可供python代码调用（windows平台）。样例见test.py

espprc问题是分支定价法解VRP时的子问题，针对VRPTW子问题的求解算法中，脉冲算法是一种比较高效的算法。
上述封装的一个明显缺陷是：每一次求解espprc问题时都要重新建图。如果想避免这一点，需要对原始C++代码中的graph类也提供python接口，这样一来工作量会变大，以后有机会再做这个。
