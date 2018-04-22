public class AbstractFactoryPatternDemo {
	public static void main(String[] args) {
		// shape factory
		AbstractFactory shapeFactory = FactoryProducer.getFactory("SHAPE");

		// circle
		Shape circle = shapeFactory.getShape("CIRCLE");
		circle.draw();

		// rectangle
		Shape rectangle = shapeFactory.getShape("RECTANGLE");
		rectangle.draw();

		// square
		Shape square = shapeFactory.getShape("SQUARE");
		square.draw();


		// color factory
		AbstractFactory colorFactory = FactoryProducer.getFactory("COLOR");

		// red
		Color red = colorFactory.getColor("RED");
		red.fill();

		// green
		Color green = colorFactory.getColor("GREEN");
		green.fill();

		// blue
		Color blue = colorFactory.getColor("BLUE");
		blue.fill();
	}
}
