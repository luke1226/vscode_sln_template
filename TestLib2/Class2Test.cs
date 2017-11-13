using System;
using Xunit;

namespace TestLib2
{
    public class Class2Test
    {
        [Fact]
        public void FailedTest1()
        {
            Assert.True(false);
        }

        [Fact]
        public void FailedTest2()
        {
            Assert.True(false);
        }

        [Fact]
        public void FailedTest3()
        {
            AssertMethod();
        }

        private void AssertMethod()
        {
            Assert.True(false);
        }
    }
}
