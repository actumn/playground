public class FactoryPatternDemo {

	public static void main(String[] args) {
		ShapeFactory shapeFactory = new ShapeFactory();

		// circle
		Shape circle = shapeFactory.getShape("CIRCLE");
		circle.draw();

		// rectangle
		Shape rectangle = shapeFactory.getShape("RECTANGLE");
		rectangle.draw();

		// square
		Shape square = shapeFactory.getShape("SQUARE");
		square.draw();
	}
}
