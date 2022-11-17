from flask import Flask, request, jsonify

app=Flask(__name__)                             #object of Flask class __name__ is used for imputing the function when called. 


@app.route('/xyz', methods=['GET','POST'])                                    #annoting the function Get=send data through url, POST= send data through body
def test():
    if request.method=='POST':
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify(str(result))

@app.route('/abc',methods=['GET','POST'])
def test1():
    if request.methods=='POST':
        a=request.json['num3']
        b=request.json['num4']
        result=a-b
        return jsonify(str(result))

@app.route('/def',methods=['GET','POST'])
def test2():
    if request.method=='POST':
        a=request.json['num5']
        b=request.json['num6']
        result=a*b
        return jsonify(str(result))

@app.route('/ghi',methods=['GET','POST'])
def test3():
    if request.method=='POST':
        a=request.json['num1']
        b=request.json['num2']
        result=a/b
        return jsonify(str(result))


if __name__=='__main__':
    app.run()
