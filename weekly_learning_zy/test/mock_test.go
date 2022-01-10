package test
import (
"testing"
"github.com/golang/mock"
)

type MyMockedObject struct{
    mock.Mock
}

func (m *MyMockedObject) DoSomething(number int) (bool, error) {
    args := m.Called(number)
    return args.Bool(0), args.Error(1)

}

func TestSomething(t *testing.T) {
    testObj := new(MyMockedObject)

    testObj.On("DoSomething", 123).Return(true, nil)

    testMockObj(testObj)

    testObj.AssertExpectations(t)
}

func testMockObj(mcObj *MyMockedObject) {
    fmt.Println(mcObj.DoSomething(123))
}