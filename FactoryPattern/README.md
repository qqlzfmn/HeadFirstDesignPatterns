# 简单工厂模式
### 定义
简单工厂其实不是一个设计模式，而是一种编程习惯。
### 模式功能
将客户程序从具体类解耦合。
### 参考
* [Python设计模式 - 简单工厂模式](http://www.isware.cn/python-design-pattern/01-simple-factory/)



# 工厂方法模式
### 定义
工厂方法模式定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个。工厂方法让类把实例化推迟到子类。
### 模式功能
将产品的「实现」从「使用」中解耦合。
### 使用场景
* 需要将类的实例化（对象的创建）封装起来的场景
### UML类图
![工厂模式](http://www.runoob.com/wp-content/uploads/2014/08/factory_pattern_uml_diagram.jpg)
### 参考
* [Python设计模式 - 工厂方法模式](http://www.isware.cn/python-design-pattern/02-factory-method/)
* [常见设计模式的定义，应用场景和方法](https://www.jianshu.com/p/f3c76b695167)
* [工厂模式|菜鸟教程](http://www.runoob.com/design-pattern/factory-pattern.html)



# 抽象工厂模式
### 定义
抽象工厂模式提供一个接口，用于创建相关或依赖对象的家族，而不需要明确指定具体类。
### 设计原则
* 要依赖抽象，不要依赖具体类。
### 模式功能
将具体产品与客户解耦合。
### 使用场景
* 将对象创建的过程封装起来，以便将代码从具体类解耦。
### UML类图
![抽象工厂模式](http://www.runoob.com/wp-content/uploads/2014/08/abstractfactory_pattern_uml_diagram.jpg)
### 参考
* [常见设计模式的定义，应用场景和方法](https://www.jianshu.com/p/f3c76b695167)
* [抽象工厂模式|菜鸟教程](http://www.runoob.com/design-pattern/abstract-factory-pattern.html)
