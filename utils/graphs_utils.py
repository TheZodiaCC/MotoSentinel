from models import Accelerometer
import io
import base64
from datetime import datetime, timedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def get_acceleration_data(time_range):
    accelerometer_data = Accelerometer.query.all()

    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for data in accelerometer_data:
        if datetime.now() - timedelta(hours=time_range) <= data.timestamp:
            timestamps.append(data.timestamp)
            x_values.append(data.x_value)
            y_values.append(data.y_value)
            z_values.append(data.z_value)

    return timestamps, x_values, y_values, z_values


def generate_acceleration_2d_graphs():
    graphs = []

    timestamps, x_values, y_values, z_values = get_acceleration_data(1)

    graphs.append(generate_2d_graph(timestamps, x_values, "x-axis acceleration", "time", "acceleration"))
    graphs.append(generate_2d_graph(timestamps, y_values, "y-axis acceleration", "time", "acceleration"))
    graphs.append(generate_2d_graph(timestamps, z_values, "z-axis acceleration", "time", "acceleration"))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def generate_2d_graph(x_points, y_points, title, x_title, y_title):
    fig = Figure()
    fig.set_dpi(150)

    axis = fig.add_subplot(1, 1, 1)

    axis.set_title(title)
    axis.set_xlabel(x_title)
    axis.set_ylabel(y_title)
    axis.grid()

    axis.plot(x_points, y_points)

    return fig


def encode_graph(fig):
    png_image = io.BytesIO()
    FigureCanvas(fig).print_png(png_image)

    encoded_png_string = "data:image/png;base64,"
    encoded_png_string += base64.b64encode(png_image.getvalue()).decode("utf8")

    return encoded_png_string