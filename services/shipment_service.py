class ShipmentService:
    def __init__(self):
        self.shipments = {}
        self.tracking_info = {}

    def create_shipment(self, shipment_id, details):
        self.shipments[shipment_id] = details
        self.tracking_info[shipment_id] = {'status': 'Created', 'location': 'Warehouse', 'timestamp': '2026-04-15 16:39:34'}

    def update_status(self, shipment_id, new_status):
        if shipment_id in self.shipments:
            self.tracking_info[shipment_id]['status'] = new_status
            self.tracking_info[shipment_id]['timestamp'] = '2026-04-15 16:39:34'
        else:
            raise ValueError('Shipment ID does not exist.')

    def track_shipment(self, shipment_id):
        if shipment_id in self.tracking_info:
            return self.tracking_info[shipment_id]
        else:
            return 'Shipment ID not found.'

    def get_analytics(self):
        return {
            'total_shipments': len(self.shipments),
            'in_transit': sum(1 for info in self.tracking_info.values() if info['status'] == 'In Transit'),
            'delivered': sum(1 for info in self.tracking_info.values() if info['status'] == 'Delivered')
        }